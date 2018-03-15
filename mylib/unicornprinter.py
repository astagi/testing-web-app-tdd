
ERR  = 'E'
WARN = 'W'

def uniformat(message, msg_type=None):
    if msg_type == ERR:
        return '🚨 {0}'.format(message)
    elif msg_type == WARN:
        return '⚠️ {0}'.format(message)
    else:
        return '🦄 {0}'.format(message)