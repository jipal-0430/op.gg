import requests

ASSASSIN = ['Nocturne', 'Shaco', 'Akali', 'Ekko', 'Evelynn', 'Fizz', 'Katarina', 'Khazix', 'Yone', 'Zed', 'Kassadin', 'Talon','Qiyana','Nidalee'] #15
SKIRMISHER = ['Gwen', 'Belveth', 'Fiora', 'Jax', 'MasterYi', 'Nilah', 'Riven', 'Tryndamere', 'Viego', 'Yasuo'] #10
JUGGERNAUT = ['DrMundo','Garen','Illaoi','Mordekaiser','Nasus','Olaf','Shyvana','Udyr','Yorick','Trundle','Skarner','Volibear','Darius','Sett','Urgot'] #15
DIVER = ['Diana','Aatrox','Camille','Irelia','JarvanIV','LeeSin','Elise','RekSai','Vi','Warwick','Wukong','XinZhao','Pantheon','Kled','Rengar','Hecarim','Nilah','Belveth','Lillia'] #19
BURST = ['Ahri','Annie','Brand','Leblanc','Lissandra','Orianna','Veigar','TwistedFate','Syndra','Neeko','Vex'] #11
BATTLEMAGE = ['Anivia','AurelionSol','casiiopeia','Karthus','Malzahar','Ryze','Swain','Taliyah','VikTor','Vladimir','Rumble','Sylas','Fiddlesticks'] #13
ARTILLERY = ['Lux','Varus','Velkoz','Xerath','Ziggs','Jayce','Zoe'] #7
INFIGHTER = ['Akshan','Aphelisos','Draven','Lucian','Samira','Tristana','Vayne','Xayah','Zeri','Kaisa','Kalista','Quinn','Kinderd'] #13
KITER = ['Varus','Ashe','Caitlyn','Ezreal','Jhin','Jinx','Kogmaw','MissFortune','Senna','Sivir'] #10
ENCHANTER = ['Sona','Soraka','Nami','Lulu','Karma','Janna','Seraphine','Yuumi','Zilean','Renata'] #10
CATCHER = ['Blitzcrank','Morgana','Ivern','Zyra','Rakan','Thresh','Bard'] #7
VANGUARD = ['Alistar','Amumu','Gnar','Gragas','Malphite','Maokai','Nautilus','Ornn','Rammus','Rell','Sejuani','Sion','Zac','Leona'] #14
WARDEN = ['Braum','Galio','Poppy','Shen','TahmKench','Trundle','Taric','Chogath'] #8
HYBRID = ['Graves','Kayle','Kennen','Pyke','Kayn'] #5
FORTRESS = ['Azir','Heimerdinger','Singed','Gangplank','Teemo'] #5
TYPE = [ASSASSIN, SKIRMISHER, JUGGERNAUT, DIVER, BURST, BATTLEMAGE, ARTILLERY, INFIGHTER, KITER, ENCHANTER, CATCHER, VANGUARD, WARDEN, HYBRID, FORTRESS]
TOP = ['원딜 분쇄기','믹서기','레이드 보스','공방일체','핵폭탄','대장군','대륙간 탄도미사일','히트맨','스나이퍼','어머니','제압자','돌격대장','장판파', '스페셜리스트', '요새']
MIDDLE =['기동형 암살자', '전투형 암살자', '돌격형 전사', '기동형 전사', '집중형 마법사', '광역형 마법사', '견재형 마법사', '기동형 원딜', '견재형 원딜', '강화형 서폿', '포획형 서폿', '공격형 탱커', '수비형 탱커', '하이브리드', '장악자']
BOTTOM = ['손가락 차이','Science','뚜벅이','자살특공대','CC셔틀','','유리물총','빠른 숟가락','긴 숟가락','혜지','Tool','전방 샌드백','후방 샌드백', '반푼이', '방구석 여포']
count_type = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

print('닉네임을 입력해주세요 > ', end='')
nickname = input()
a = nickname.lower().replace(' ','')

API_KEY = 'RGAPI-dc94c5e8-e203-4bfe-884f-b4739150c319'

get_puuid_url = f'https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/{nickname}?api_key={API_KEY}'
response = requests.get(get_puuid_url)
puuid = response.json()['puuid']

get_list_of_match_id_url = f'https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?api_key={API_KEY}'
response = requests.get(get_list_of_match_id_url)
win_rate = 0

test = {}

for match_id in response.json():
     get_match_by_match_id_Head = 'https://asia.api.riotgames.com/lol/match/v5/matches/'
     get_match_by_match_id_url = f'{get_match_by_match_id_Head}{match_id}?api_key={API_KEY}'
     response = requests.get(get_match_by_match_id_url)
     
     for participant in response.json()['info']['participants']:
          b = participant['summonerName'].lower().replace(' ','')
          win = participant['win']
          champion_name = participant['championName']
          if b==a:
               print(participant['championName'], int(win))
               win_rate += int(win)

               for i in range(15):
                    if champion_name in TYPE[i]:
                         count_type[i] += 1



win_rate *= 5
print(f"{nickname}의 최근 20경기 전적 승률은 {win_rate}% 입니다")
print(count_type)

max_index = 0
max_value = 0

for i in range(15):
     if count_type[i] > max_value:
          max_index = i
          max_value = count_type[i]


if win_rate >= 65:
     print(TOP[max_index])
elif win_rate >= 45:
     print(MIDDLE[max_index])
else:
     print(BOTTOM[max_index])



""""
if tier == '상위':
     print('대마법사')
elif tier == '중간':
     print('메이지')
else:
     print('궁싸개')
"""