
def uniformat(message, msg_type=None):
    if msg_type == 'E':
        return '🚨 {0}'.format(message)
    else:
        return '🦄 {0}'.format(message)