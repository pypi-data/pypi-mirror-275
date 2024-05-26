from typing import List
from bibtexparser.splitter import Splitter
from bibtexparser.model import Entry, Field
from bibtexparser.writer import BibtexFormat, VAL_SEP, _val_intent_string
from bibtexparser.exceptions import BlockAbortedException, ParserStateException
import logging
import re

# Overwriting bibtexparser.Splitter to return an Entry.
class EntrySplitter(Splitter):

    def split(self) -> Entry:      

        self._markiter = re.finditer(
            r"(?<!\\)[\{\}\",=\n]|@[\w]*( |\t)*(?={)", self.bibstr, re.MULTILINE
        )

        while True:
            m = self._next_mark(accept_eof=True)
            if m is None:
                break

            m_val = m.group(0).lower()

            if m_val.startswith("@"):
                # Clean up previous block implicit_comment
                implicit_comment = self._end_implicit_comment(m.start())
                if implicit_comment is not None:
                    pass
                self._implicit_comment_start = None

                start_line = self._current_line
                try:
                    # Start new block parsing
                    if m_val.startswith("@comment"):
                        pass
                    elif m_val.startswith("@preamble"):
                        pass
                    elif m_val.startswith("@string"):
                        pass
                    else:
                        entry = self._handle_entry(m, m_val)

                except BlockAbortedException as e:
                    logging.warning(
                        f"Parsing of `{m_val}` block (line {start_line}) "
                        f"aborted on line {self._current_line} "
                        f"due to syntactical error in bibtex:\n {e.abort_reason}"
                    )
                    logging.info(
                        "We will try to continue parsing, but this might lead to unexpected results."
                    )

                except ParserStateException as e:
                    # This is a bug in the parser, not in the bibtex. We should not continue.
                    logging.error(
                        "python-bibtexparser detected an invalid state. Please report this bug."
                    )
                    logging.error(e.message)
                    raise e
                except Exception as e:
                    # For unknown exeptions, we want to fail hard and get the info in our issue tracker.
                    logging.error(
                        f"Unexpected exception while parsing `{m_val}` block (line {start_line})"
                        "Please report this bug."
                    )
                    raise e

                self._reset_block_status(current_char_index=self._current_char_index + 1)
            else:
                # Part of implicit comment
                continue

        # Check if there's an implicit comment at the EOF
        if self._implicit_comment_start is not None:
            comment = self._end_implicit_comment(len(self.bibstr))
            if comment is not None:
                pass

        return entry

# Taken from https://github.com/sciunto-org/python-bibtexparser/blob/main/bibtexparser/writer.py#L41
# Modified slightly to use here without having to specify a bibtex_format as in the original and 
# to return a concatenated string at the end.
def getEntryRaw(block: Entry) -> List[str]:
    res = ["@", block.entry_type, "{", block.key, ",\n"]
    bibtex_format = BibtexFormat()
    field: Field
    for i, field in enumerate(block.fields):
        res.append(bibtex_format.indent)
        res.append(field.key)
        res.append(_val_intent_string(bibtex_format, field.key))
        res.append(VAL_SEP)
        res.append(field.value)
        if bibtex_format.trailing_comma or i < len(block.fields) - 1:
            res.append(",")
        res.append("\n")
    res.append("}\n")
    
    return "".join(res)
