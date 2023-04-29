import vk_api
import requests

def open_settings():
    with open('settings.txt') as f:
        s, n = f.readlines()
        return {'TOKEN' : s.split(' : ')[1], 'GROUP_ID' : int(n.split(' : ')[1])}

def main():
    try:
        config = open_settings()
        vk_session = vk_api.VkApi(token= config['TOKEN'])
        vk = vk_session.get_api()
        
        data = vk.stories.get(owner_id=0-abs(config['GROUP_ID']), extended=1, v=5.131)['items'][0]
        # account = vk.account.getProfileInfo()
        # if account['id'] == 478627686:
        #     account = True
        # else:
        #     account = False
        # print(account)
        name = data['name']
        urls = []
        for elem in data['stories']:
            url = (elem['video']['files'][list(elem['video']['files'].keys())[0]]).split('?')[0]
            urls.append(url)
        print(f'Всего историй в группе "{name}": {len(urls)}')
        # if account:
        print('Скачивание началось...')
        k = 1
        for url in urls:
            req = requests.get(url)
            with open(f'videos/{name}{k}.mp4', 'wb') as f:
                f.write(req.content)
            print(f'Видео {k} скачано')
            k += 1
        # else:
        #     print('Спасибо!')

    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
