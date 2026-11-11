"""Игры и викторины — самостоятельный первый сценарий."""
HELP = '/question вопрос | ответ — добавить (админ)\n/list — вопросы\n/answer ID | ответ — ответить один раз\n/score — мои очки'

def handle(s, u, cmd, arg, admin):
    from core import require_admin, parts, positive, add, item, listing

    if cmd == '/question':
        require_admin(admin)
        title, answer = parts(arg,2)
        return 'Создано #' + add(s, title=title, answer=answer.casefold(), attempts={})
    if cmd == '/list': return listing(s)
    if cmd == '/answer':
        key, answer = parts(arg,2)
        row = item(s,key)
        if u in row['attempts']: raise ValueError('Вы уже отвечали.')
        correct = answer.casefold() == row['answer']
        row['attempts'][u] = correct
        return 'Верно! +1 очко.' if correct else 'Неверно. Попытка использована.'
    if cmd == '/score': return 'Очки: ' + str(sum(int(x['attempts'].get(u,False)) for x in s.get('items',{}).values()))
