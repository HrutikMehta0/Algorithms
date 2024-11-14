def reorderLogFiles(logs):
        digit_log = []
        letter_log = []
        for log in logs:
            if log[-1].isdigit():
                digit_log.append(log)
            else:
                letter_log.append(log)
        letter_log.sort(key= lambda x:(x.split()[1:], x.split()[0]))
        result = letter_log + digit_log
        return result