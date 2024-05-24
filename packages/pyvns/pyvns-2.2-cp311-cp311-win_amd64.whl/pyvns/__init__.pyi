from .vns_python_wrapper import Compiler as Compiler, Dialogue as Dialogue, DialoguesManager as DialoguesManager, Event as Event, Naming as Naming
from _typeshed import Incomplete

dialogue_data_t: Incomplete
dialogue_section_t = dict[str, dialogue_data_t]
dialogue_content_t = dict[str, dialogue_section_t]
