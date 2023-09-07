from typing import Dict, List, Union

from Yukki import db

assisdb = db.assistantmultimode


async def get_as_names(chat_id: int) -> List[str]:
    _notes = []
    for note in await _get_assistant(chat_id):
        _notes.append(note)
    return _notes


async def _get_assistant(chat_id: int) -> Dict[str, int]:
    _notes = await assisdb.find_one({"chat_id": chat_id})
    if not _notes:
        return {}
    return _notes["notes"]


async def get_assistant(chat_id: int, name: str) -> Union[bool, dict]:
    name = name.lower().strip()
    _notes = await _get_assistant(chat_id)
    if name in _notes:
        return _notes[name]
    else:
        return False


async def save_assistant(chat_id: int, name: str, note: dict):
    name = name.lower().strip()
    
    # Serialize the note object to a dictionary
    note_dict = {
        "field1": note.field1,  # Replace with actual field names from the note object
        "field2": note.field2,
        # Add more fields as needed
    }
    
    _notes = await _get_assistant(chat_id)
    _notes[name] = note_dict  # Store the serialized note
    
    await assisdb.update_one(
        {"chat_id": chat_id}, {"$set": {"notes": _notes}}, upsert=True
    )

