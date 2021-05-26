def block(text, mention_id=None):
    if mention_id:
        return '<@%s>\n%s' % (mention_id, text)
    else:
        return text


def code_block(text, mention_id=None):
    return block('```%s```' % (text,), mention_id=mention_id)
