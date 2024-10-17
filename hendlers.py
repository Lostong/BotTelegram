from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message


import keyboard as kb


router = Router()
#роутер для старту і button меню
@router.message(CommandStart())
async def start(message: Message) -> None:
        await message.reply(
        f"Привіт, я Назар (розробник цього бота).\n"
        f"Коли я проходив Metro Exodus я багато чого не знав і через це проходження затягнулося на довго\n"
        f"Тож, щоб не повторювати мої похибки, пропоную вам ознайомитись з моїм ботом-посібником по цій чудовій грі\n"
        f"Ну що ж приступимо, напиши Меню для початку",
        reply_markup=kb.setting)
@router.message(F.text == "Меню")
async def menu(message:Message) -> None:
    await message.answer("Ось головне меню",
        reply_markup=kb.main)
#Ці роутери для Схожі ігри
@router.message(F.text == "Схожі ігри")
async def any_game(message: Message) -> None:
        await message.answer("Ви обрали Схожі ігри",
        reply_markup=kb.games)
@router.message(F.text == "Інші ігри")
async def any_games(message:Message) ->None:
        await message.answer(text="https://store.steampowered.com/recommended/morelike/app/412020/")
@router.message(F.text == "S.T.A.L.K.E.R.")
async def stalker(message:Message) ->None:
        await message.answer(f"S.T.A.L.K.E.R. — серія відеоігор, розроблена та випущена українською компанією GSC Game World.\n"
                             f" Створена в жанрі шутер від першої особи з елементами survival horror та рольової гри.\n"
                             f" Події гри відбуваються в наш час, в альтернативному світі на території України, в Чорнобильській зоні відчуження. ")
        await message.answer("Що б дізнатись детальніше переходь по посиланю")
        await message.answer(text="https://store.steampowered.com/franchise/stalker?l")
@router.message(F.text == "Fallout 4")
async def folaut(message:Message) ->None:
        await message.answer(f"Fallout 4 — відеогра жанру Action/RPG, сиквел Fallout 3, розроблена Bethesda Game Studios.\n"
                             f" Гра є п'ятою канонічною частиною серії, і була анонсована 3 червня 2015 року.\n"
                             f" Вихід відбувся для платформ PC, PS4 та Xbox One 10 листопада 2015 року.\n"
                             f" Події розгортаються через 200 років після ядерної війни в околицях Бостона.")
        await message.answer("Що б дізнатись детальніше переходь по посиланю")
        await message.answer(text="https://store.steampowered.com/app/377160/Fallout_4/")
@router.message(F.text == "Dying Light")
async def dying_light(message:Message) ->None:
        await message.answer(f"Dying Light — відеогра з відкритим ігровим світом від першої особи в жанрах Action-adventure/Survival horror, створена польським розробником відеоігор Techland і видана Warner Bros.\n"
                             f" Анонсована в травні 2013 року, а вийшла в січні 2015 для Microsoft Windows, Linux, PlayStation 4 і Xbox One.\n")
        await message.answer("Що б дізнатись детальніше переходь по посиланю")
        await message.answer(text="https://store.steampowered.com/app/239140/Dying_Light/")
@router.message(F.text == "The Last of Us Part II")
async def the_las_of_as(message:Message) ->None:
        await message.answer(f"The Last of Us Part II — відеогра жанру action-adventure з елементами survival horror і стелс-екшену від третьої особи.\n"
                             f" Розроблена Naughty Dog і видана Sony Interactive Entertainment ексклюзивно для ігрової консолі PlayStation 4 19 червня 2020 року.")
        await message.answer("Що б дізнатись детальніше переходь по посиланю")
        await message.answer(text="https://store.playstation.com/ru-ua/product/EP9000-CUSA10249_00-THELASTOFUSPART2")
@router.message(F.text == "Horizon Zero Dawn")
async def Horizon_Zero_Dawn(message:Message) ->None:
        await message.answer(f"Horizon Zero Dawn — відеогра жанру Action/RPG, розроблена студією Guerrilla Games і видана Sony Interactive Entertainment 28 лютого 2017 року для PlayStation 4.\n"
                             f" 7 серпня 2020 року гра вийшла на платформі Windows.\n"
                             f" Продовження, Horizon Forbidden West, вийшло для PlayStation 4 і PlayStation 5 18 лютого 2022 року.")
        await message.answer("Що б дізнатись детальніше переходь по посиланю")
        await message.answer(text="https://store.steampowered.com/app/1151640/Horizon_Zero_Dawn_Complete_Edition/")
@router.message(F.text == "Chernobylite")
async def Chernobylite(message:Message) ->None:
        await message.answer(f"Chernobylite — науково-фантастична відеогра, симулятор виживання, розроблена польською студією Farm 51 і опублікована All in! Games.\n"
                             f" Реліз відбувся для платформ Microsoft Windows, PlayStation 4, PlayStation 5, Xbox One і Xbox Series X/S в 2021 році.")
        await message.answer("Що б дізнатись детальніше переходь по посиланю")
        await message.answer(text="https://store.steampowered.com/app/1016800/Chernobylite_Complete_Edition/")
#Ці роутери для Чому варто пограти
@router.message(F.text == "Чому варто пограти")
async def how_game(message:Message) -> None:
    await message.answer(f"Захоплюючий постапокаліптичний сюжет\n"
                         f"Атмосферу виживання з обмеженими ресурсами.\n"
                         f"Відкритий світ із різноманітними локаціями.\n"
                         f"Комбінацію стелсу, екшену та дослідження.\n"
                         f"Вражаючу графіку й деталізацію.")
    await message.answer(text="https://www.reddit.com/r/Ukraine_UA/comments/14t5579/metro_exodus_чи_грав_хтось_цю_відеогру_чи_варто/")
#Ці роутери для Місії
@router.message(F.text == "Місії")
async def mision(message:Message) -> None:
    await message.answer("оберіть одну з місій",
    reply_markup=kb.mision)
@router.message(F.text == "Москва")
async def Moscow(message:Message) -> None:
    await message.answer(f"Короткий опис:\n"
                         f" Місія розпочинається в метро, де Артем продовжує шукати життя за межами метро.\n"
                         f"Події приводять його до того, що він знаходить поверхню Москви, а потім рятується від сил Червоного лінії та Ордена, намагаючись вирватися назовні.\n"
                         f"Як пройти:\n"
                         f" Ця місія лінійна з акцентом на виживання та стелс.\n"
                         f"Гра нагадує попередні частини серії Metro.\n"
                         f" Варто діяти тихо, щоб не привертати зайву увагу мутантів.")
@router.message(F.text == "Волга")
async def Volga(message: Message) -> None:
    await message.answer(f"Короткий опис:\n"
                         f" Після втечі з Москви Артем і його команда прибувають на річку Волгу.\n"
                         f"Тут їм доведеться взаємодіяти з місцевими мутантами та релігійною сектою, яка не приймає технології.\n"
                         f"Як пройти:\n"
                         f" Це перша велика відкрито-світова місія.\n"
                         f"Тобі потрібно досліджувати, шукати ресурси та виконувати квести.\n"
                         f"Можна використовувати човен для переміщення по річці.")

@router.message(F.text == "Ямантау")
async def Yamantau(message: Message) -> None:
    await message.answer(f"Короткий опис:\n"
                         f" Артем та команда вирушають на базу Ямантау, сподіваючись знайти вижилих урядовців.\n"
                         f"Проте вони виявляють, що база контролюється канібалами.\n"
                         f"Як пройти:\n"
                         f" Лінійний рівень, де потрібно боротися з численними ворогами в коридорах бази.\n"
                         f"Досліджуй кожен куточок для збору ресурсів.")

@router.message(F.text == "Каспій")
async def Caspian(message: Message) -> None:
    await message.answer(f"Короткий опис:\n"
                         f" Артем і його група опиняються в пустельних районах Каспійського моря.\n"
                         f"Тут їм доведеться боротися з мародерами та виживати в умовах нестачі води.\n"
                         f"Як пройти:\n"
                         f" Велика і відкрита місія з численними квестами.\n"
                         f"Ти можеш досліджувати пустелю на автомобілі.")

@router.message(F.text == "Тайга")
async def Taiga(message: Message) -> None:
    await message.answer(f"Короткий опис:\n"
                         f" Після аварії поїзда Артем опиняється в густому лісі.\n"
                         f"Йому доведеться зіткнутися з місцевими вижилими та дикими звірами.\n"
                         f"Як пройти:\n"
                         f" Місія побудована на стелсі.\n"
                         f"Стелс допоможе уникнути зайвих конфліктів з добре озброєними ворогами.")

@router.message(F.text == "Мертве місто")
async def DeadCity(message: Message) -> None:
    await message.answer(f"Короткий опис:\n"
                         f" Фінальна місія гри. Артем і команда прибувають до зруйнованого міста після атомної катастрофи.\n"
                         f"Їм необхідно знайти ліки для поранених.\n"
                         f"Як пройти:\n"
                         f" Місія сповнена небезпечними мутантами та зараженими ділянками.\n"
                         f"Дій обережно, досліджуй та виживай, не забуваючи про фільтри для протигаза.")
#Ці роутери для кінцівок
@router.message(F.text == "Усі кінцівки")
async def good_ending(message: Message) -> None:
    await message.answer("Оберіть який вам потрібен фінал",
    reply_markup=kb.end)
@router.message(F.text == "Оптимістичний фінал")
async def good_ending(message: Message) -> None:
    await message.answer(f"Умови:\n"
                         f"Гравець повинен здійснити велику кількість позитивних дій, зокрема, проявляти співчуття та допомагати іншим.\n"
                         f"Наприклад, гравець може відмовитися від насильства у взаємодії з ворогами, вибираючи стелс-методи, а також проявляти доброту до персонажів, таких як Діма.\n"
                         f"Опис:\n"
                         f"Артем та його команда знаходять нову домівку в безпечному місці, де вони можуть почати нове життя.\n"
                         f"У цьому фіналі спостерігається відновлення надії на майбутнє, і Артем відчуває, що його мета досягнута.")
@router.message(F.text == "Песимістичний фінал")
async def bad_ending(message: Message) -> None:
    await message.answer(f"Умови:\n"
                         f"Гравець здійснює багато негативних дій, включаючи вбивства без потреби, не допомагає союзникам та проявляє агресію в стосунках із персонажами.\n"
                         f"Опис:\n"
                         f"У цьому фіналі Артем та його команда виявляються в безвихідній ситуації, де панує відчай і темрява.\n"
                         f"Вони не можуть знайти безпечне місце, і гравець може бачити, як їхня мрія про нове життя розпадається.")
@router.message(F.text == "Фінал з Дімою")
async def dima_ending(message: Message) -> None:
    await message.answer(f"Умови:\n"
                         f"Гравець повинен проявляти доброту до Діми, жертвуючи собою, щоб врятувати Артема.\n"
                         f"Опис:\n"
                         f"Якщо Діма жертвує собою, фінал буде оптимістичним, навіть якщо гравець вчинить деякі негативні дії.\n"
                         f"Фінал залишає гравця з почуттям надії, адже Артем отримує шанс продовжити своє життя.")
@router.message(F.text == "Фінал з Мілею")
async def milya_ending(message: Message) -> None:
    await message.answer(f"Умови:\n"
                         f"Гравець має підтримувати хороші відносини з Мілею, проявляючи до неї доброту та увагу.\n"
                         f"Опис:\n"
                         f"Якщо Артем та Міля залишаються близькими, фінал буде м'якшим і добрішим, навіть якщо не всі вибори будуть позитивними.\n"
                         f"Це створює відчуття завершеності та розуміння, що вони можуть впоратися з усіма труднощами разом.")
#Ці роутери для досягнень
@router.message(F.text == "Досягнення")
async def achiv(message:Message) -> None:
    await message.answer("Оберіть досягення яке цікавить",
                         reply_markup=kb.achivm)
@router.message(F.text == "Паспорт")
async def passport(message:Message) -> None:
    await message.answer(f"Опис:\n"
                         f" Завершити гру.\n"
                         f"Як отримати:\n"
                         f" Пройди всі місії гри до кінця.")
@router.message(F.text == "Не забудь про нас")
async def dont_forget(message: Message) -> None:
    await message.answer(f"Опис:\n"
                         f"Знайти та відновити фотографію з Клавою.\n"
                         f"Як отримати:\n"
                         f"У місії 'Волга' знайди фотографію в одному з будинків на березі річки.")
@router.message(F.text == "Смертельний холод")
async def deadly_cold(message: Message) -> None:
    await message.answer(f"Опис:\n"
                         f"Пережити перший напад Буревію.\n"
                         f"Як отримати:\n"
                         f"Дотримуйся обережності під час проходження місії 'Каспій' і виживай під час нападу Буревію.")
@router.message(F.text == "Вирушай у мандри")
async def on_the_road(message: Message) -> None:
    await message.answer(f"Опис:\n"
                         f"Завершити перший етап подорожі.\n"
                         f"Як отримати:\n"
                         f"Успішно пройди через місію 'Москва'.")
@router.message(F.text == "Спостерігач")
async def observer(message: Message) -> None:
    await message.answer(f"Опис:\n"
                         f"Знайти всі щоденники та записки.\n"
                         f"Як отримати:\n"
                         f"Під час гри знаходь всі записки та щоденники на локаціях.")
@router.message(F.text == "Грішник")
async def sinner(message: Message) -> None:
    await message.answer(f"Опис:\n"
                         f"Знищити певну кількість ворогів у грі.\n"
                         f"Як отримати:\n"
                         f"Убий велику кількість ворогів на різних етапах гри.")
@router.message(F.text == "Тихий вбивця")
async def silent_assassin(message: Message) -> None:
    await message.answer(f"Опис:\n"
                         f"Завершити місію, не викликавши тривоги.\n"
                         f"Як отримати:\n"
                         f"Використовуй стелс для усунення ворогів, щоб не привертати уваги.")
@router.message(F.text == "Секрети")
async def secrets(message: Message) -> None:
    await message.answer(f"Опис:\n"
                         f"Знайти всі таємні локації.\n"
                         f"Як отримати:\n"
                         f"Досліджуй кожну локацію та шукай сховані кімнати або секції.")
@router.message(F.text == "Снайпер")
async def sniper(message: Message) -> None:
    await message.answer(f"Опис:\n"
                         f"Знищити ворога на великій дистанції.\n"
                         f"Як отримати:\n"
                         f"Використовуй снайперську гвинтівку і стріляй у ворога з великої відстані.")
@router.message(F.text == "Найкращий друг")
async def best_friend(message: Message) -> None:
    await message.answer(f"Опис:\n"
                         f"Підтримати Діму у всіх його спробах.\n"
                         f"Як отримати:\n"
                         f"Проявляй доброту до Діми в його ситуаціях.")
@router.message(F.text == "Мисливець за скарбами")
async def treasure_hunter(message: Message) -> None:
    await message.answer(f"Опис:\n"
                         f"Знайти всі артефакти.\n"
                         f"Як отримати:\n"
                         f"Досліджуй всі локації та шукай артефакти.")
@router.message(F.text == "Секрети народу")
async def peoples_secrets(message: Message) -> None:
    await message.answer(f"Опис:\n"
                         f"Дослідити всі основні місії.\n"
                         f"Як отримати:\n"
                         f"Завершуй всі основні квести, звертаючи увагу на діалоги та подробиці.")
@router.message(F.text == "Переможець")
async def victor(message: Message) -> None:
    await message.answer(f"Опис:\n"
                         f"Завершити гру на рівні складності 'Хардкор'.\n"
                         f"Як отримати:\n"
                         f"Пройди гру на складному рівні, не використовуючи збереження.")
@router.message(F.text == "Життя за життя")
async def life_for_life(message: Message) -> None:
    await message.answer(f"Опис:\n"
                         f"Врятувати союзника під час місії.\n"
                         f"Як отримати:\n"
                         f"Під час проходження рівнів, рятуй персонажів, які потребують допомоги.")
@router.message(F.text == "Тотальна війна")
async def total_war(message: Message) -> None:
    await message.answer(f"Опис:\n"
                         f"Убий понад 100 ворогів за гру.\n"
                         f"Як отримати:\n"
                         f"Залишайся агресивним і вбивай ворогів у всіх можливих місіях.")
#ці роутери відповідають за зворотній звязок
@router.message(F.text == "Зворотній звязок")
async def zvorortniy_zvyazok(message:Message) -> None:
    await message.answer("Що б повідомити про помилку або ідеї пишіть сюди\n")
    await message.answer(text="@lostongs")
#mems for IT
@router.message(F.text == "Меми для IT-шніков😂")
async def mem(message:Message) -> None:
    await message.answer("Я ПРИНОШУ СВОЇ ГЛИБОКІ ВИБАЧЕННЯ ЗА МЕМИ НА РОСІЙСЬКІЙ МОВІ")
    await message.answer("Ви обрали важки шлях, тримайтесь🫥")
    await message.answer("Скиньте будь ласка копійку на бензин(((",
                         reply_markup=kb.mems)
@router.message(F.text == "1")
async def mem1(message:Message) -> None:
    await message.answer_photo('https://instagram.fiev9-1.fna.fbcdn.net/v/t51.29350-15/442127650_1770709976674002_6361938303303336609_n.jpg?stp=dst-jpg_e35&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi44Mjh4ODI4LnNkci5mMjkzNTAuZGVmYXVsdF9pbWFnZSJ9&_nc_ht=instagram.fiev9-1.fna.fbcdn.net&_nc_cat=106&_nc_ohc=vkwxRwnPLNUQ7kNvgFFKaNd&_nc_gid=ea47156bfe0e4f388916f4579160f473&edm=ALQROFkBAAAA&ccb=7-5&ig_cache_key=MzM2MTkwMzIzOTI5MTY3OTQ5OQ%3D%3D.3-ccb7-5&oh=00_AYA3b4rWc1WSTo8xepCfMGMV3aeRZhD9BlpzC3EXoEKCnw&oe=6709B920&_nc_sid=fc8dfb.jpg')
@router.message(F.text == "2")
async def mem1(message:Message) -> None:
    await message.answer_photo('https://dev.ua/storage/images/49/03/08/06/derived/0679a4c2817dd560f6bdd0d8bd3dec3e.jpg')
@router.message(F.text == "3")
async def mem1(message:Message) -> None:
    await message.answer_photo('https://dev.ua/storage/images/44/54/24/65/derived/7964fb5c0aa7c97bb44c92d04925ab93.jpg')
@router.message(F.text == "4")
async def mem1(message:Message) -> None:
    await message.answer_photo('https://dev.ua/storage/images/16/24/45/81/derived/217a4a5a1af2c841fefaf995ba34d600.jpg')
@router.message(F.text == "5")
async def mem1(message:Message) -> None:
    await message.answer_photo('https://dev.ua/storage/images/69/59/84/91/derived/960dfc21ec413c906f91994f33bb5ce9.jpg')
@router.message(F.text == "6")
async def mem1(message:Message) -> None:
    await message.answer_photo('https://dev.ua/storage/images/29/83/89/15/derived/a341c60c8a6f935bf3c250a8b62b88e2.jpg')
@router.message(F.text == "7")
async def mem1(message:Message) -> None:
    await message.answer_photo('https://dev.ua/storage/images/53/23/73/06/derived/e9cc1aca3617c45312985ecc8ac508d7.jpg')
@router.message(F.text == "8")
async def mem1(message:Message) -> None:
    await message.answer_photo('https://dev.ua/storage/images/98/69/34/12/derived/e054dbeb2238808324f64b454aa5d01d.jpg')
@router.message(F.text == "9")
async def mem1(message:Message) -> None:
    await message.answer_photo('https://dev.ua/storage/images/92/51/04/32/derived/1c530c384b8ef5fa0d1b94c220e7bad1.jpg')
@router.message(F.text == "10")
async def mem1(message:Message) -> None:
    await message.answer_photo('https://dev.ua/storage/images/10/50/92/20/derived/c96aba43a572a2e6f5183213ab6214f5.jpg')
@router.message(F.text == "11")
async def mem1(message:Message) -> None:
    await message.answer_photo('https://dev.ua/storage/images/22/36/29/97/derived/f3d2bd6ecc1eb304a5b67537d9399920.jpg')
@router.message(F.text == "12")
async def mem1(message:Message) -> None:
    await message.answer_photo('https://dev.ua/storage/images/77/51/45/94/derived/d4d67e5116c12dba45b0c77efa2038f3.jpg')
@router.message(F.text == "13")
async def mem1(message:Message) -> None:
    await message.answer_photo('https://dev.ua/storage/images/90/03/83/81/derived/7464b606677c81fb72bdc574ba641b19.jpg')
@router.message(F.text == "14")
async def mem1(message:Message) -> None:
    await message.answer_photo('https://dev.ua/storage/images/45/91/95/25/derived/c4066ce9525acf41f5a4f2d3d9698983.jpg')
@router.message(F.text == "15")
async def mem1(message:Message) -> None:
    await message.answer_photo('https://instagram.fiev9-1.fna.fbcdn.net/v/t51.29350-15/240408661_358766302396508_2080976361463969638_n.jpg?stp=dst-jpg_e35&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xMDgweDEwODAuc2RyLmYyOTM1MC5kZWZhdWx0X2ltYWdlIn0&_nc_ht=instagram.fiev9-1.fna.fbcdn.net&_nc_cat=108&_nc_ohc=PKYKbr298DcQ7kNvgGq4syA&_nc_gid=c6124a0ac4494ecaa2566ba1f2885630&edm=AP4sbd4BAAAA&ccb=7-5&ig_cache_key=MjY0Njc2MzY5MTk1MjIwMjM1Mw%3D%3D.3-ccb7-5&oh=00_AYBiNThOlrIL5iFPb9WQSqUAikKLwBhLzE3LxHYpy5mAQw&oe=6709E6AB&_nc_sid=7a9f4b.jpg')

#Ви чуєте ехо? а воно тут є
@router.message()
async def eho(message:Message) -> None:
    await message.answer("Ви попали в аномалію (перегляньте команду яку ви написали напевно я її ще не добавив)")
































