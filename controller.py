import view as v
import model as m

def start():
    choice = ''
    while choice != 9:
        choice = v.main_menu()
        match choice:
            case 1:
                m.open_file()
            case 2:
                m.save_file()
            case 3:
                v.show_notes(m.get_notes())
            case 4:
                new_note = list(v.create_new_note())
                m.add_new_note(new_note)
            case 5:
                del_note = v.select_note('Введите название или содержание удаляемой заметки: ')
                note = m.get_note(del_note)
                if note:
                    confirm = v.delete_confirm(note[0][0])
                    if confirm:
                        m.remove_note(note[0])
                elif note == []:
                    v.empty_request()
                else:
                    v.many_request()
            case 6:
                name = v.select_note('Введите название или содержание изменяемой заметки: ')
                note = m.get_note(name)
                if note:
                    changed = v.change_note()
                    m.edit_note(note[1], list(changed))
                elif note == []:
                    v.empty_request()
                else:
                    v.many_request()
            case 7:
                find = v.find_note()
                result = m.search_note(find)
                v.show_notes(result)
            case 8:
                dt = input('Введите дату: ')
                notes = m.filter_note_by_date(dt)
                v.show_notes(notes)
            case 9:
                v.end_program()
                break