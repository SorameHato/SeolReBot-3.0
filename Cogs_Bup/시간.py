# coding: utf-8
import discord
from discord.ext import commands
from datetime import datetime as dt
from datetime import timezone as tz
from datetime import timedelta as td
from datetime import time
global guild_ids
import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from main import guild_ids
def __time__(hour, minute=0, second=0):
    return time(hour=hour,minute=minute,second=second,tzinfo=tz(td(hours=9)))

def __checkBetween__(tcode, beginHour, beginMinute, endHour, endMinute):
    return (tcode >= __time__(beginHour, beginMinute) and tcode < __time__(endHour, endMinute))

def __checkLess__(tcode, endHour, endMinute):
    return (tcode <= __time__(endHour, endMinute))

__대사__ = [ # 월요일
    [# 일 2300 ~ 월 0030
     '주말이 끝났어요... 조금 힘드시겠지만 그래도 조금만 힘을 내 주세요! 저도 힘 내서 열심히 여러분을 가시는 목적지까지 모셔다 드릴 테니까요! 화이팅이에요!',
     # 월 0630 ~ 월 0800
     '좋은 아침이에요! 월요일이라 힘들긴 하지만 그래도 상쾌한 아침이라 기분이 좋은 것 같아요. 오늘 하루도 설빈레피딕스 열차를 타고 기분 좋게, 상쾌하게 시작해요!',
     # 월 0900 ~ 월 1100
     '하늘이 참 맑죠? 하늘민국은 강수량이 적고 그마저도 겨울에 폭설로 내리는 게 대부분이라 이렇게 맨날 하늘이 파랗고 맑아요.\n월요일이라 힘드시겠지만, 이 푸른 하늘을 보면서 힘내서 열심히 일해요! 눈 깜짝할 사이에 점심시간이 올 테니까요!',
     # 월 1100~1300
     '슬슬 점심시간이네요! 오늘의 구내식당 점심은 무엇이려나요? 설빈레피딕스에서 직영하는 빛리역 구내식당은 엄청 맛있는데, 외부 업체에서 하는 서지은역 구내식당은 별로인 것 같아요.\n근데 전 이상하게 빛리승무본부보단 서지은승무본부에 배치되는 경우가 많아요... 공식 캐릭터 보정은 못 받는 걸까요?',
     # 월 1300 ~ 월 1430
     '다행히 오늘은 빛리승무본부 배속이라 맛있는 점심을 먹었어요! 배가 불러서 졸리겠지만, 힘 내서 퇴근할 때 까지 열심히 일해봐요!',
     # 월 1430~1630
     '슬슬 나른해지는 시간이에요... 월요병 때문에 더 힘든 것 같아요. 그래도 힘 낼게요! 여러분도 힘을 내 주세요!',
     # 월 1800 ~ 월 1930
     '월요일이라 월요병 때문에 힘드셨을 것 같은데, 그래도 열심히 일하시느라 수고하셨어요! 빠른 설빈레피딕스 열차를 타고 빛의 속도로 퇴근해요!',
     # 월 1930 ~ 월 2100
     '슬슬 해가 지는 것 같네요. 가벼운 산책은 어떠신가요? 전 해가 지고 난 직후의 풍경을 좋아해서, 비번인 날에는 항상 저녁을 먹고 나와서 북해 해안가 산책로를 산책하고 있어요.',
     # 월 2100 ~ 월 2300
     '이제 완전히 밤이네요. 라프텔이나 애니플러스의 찜한 작품 목록에 쌓여있는 애니를 한 편 보면서 휴식을 취하시는 건 어떠신가요?'
    ], # 화요일
    [# 월 2300 ~ 화 0030
     '오늘 하루도 수고하셨어요! 내일은 화요일.. 아직까지는 한 주의 시작이지만 그래도 벌써 평일의 20%가 지났어요! 내일도 화이팅이에요! 안녕히 주무세요!',
     # 화 0630 ~ 화 0800
     '좋은 아침이에요! 무사히 월요일을 보내고 화요일이 되었어요. 오늘 하루도 상쾌한 아침 공기를 마시면서, 설빈레피딕스 열차를 타고 기분 좋게 시작해요!',
     # 화 0900 ~ 화 1100
     '오늘도 하늘이 맑아서 다행인 것 같아요. 푸른 하늘을 보면, 저 푸른 하늘 위를 한 번 즈음 날아보고 싶다는 생각이 들어요.\n\'이 넓은 하늘에, 날개를 펴고\'에 나오는 소어링부처럼 글라이더를 타면 날 수 있을까요?',
     # 화 1100 ~ 화 1300
     '슬슬 점심시간이에요! 오늘도 맛있는 점심이 나왔으면 좋겠어요. 오늘은 서지은승무본부 배속이라 기대는 하지 않지만요.',
     # 화 1300 ~ 화 1430
     '점심은 맛있게 드셨나요? 전 결국 바깥에 나가서 샐러드를 먹었어요. 진짜로 서지은승무본부 구내식당은 돈이 아까울 정도에요!',
     # 화 1430 ~ 화 1630
     '슬슬 나른해지는 시간이에요... 그래도 오늘은 월요일이 아니라 화요일이니까, 졸음을 참고 버텨봐요! 아자아자!',
     # 화 1800 ~ 화 1930
     '오늘도 수고하셨어요! 벌써 평일의 40%가 끝나가고 있어요! 빠른 설빈레피딕스 열차를 타고 빛의 속도로 퇴근해요!',
     # 화 1930 ~ 화 2100
     '해가 지는 걸 보면 \'오늘 하루도 끝나가는구나...\' 같은 생각이 들어요. 전 오늘도 북해 해안가 산책로를 산책할 거에요. 여러분도 같이 산책하시는 게 어떠신가요?',
     # 화 2100 ~ 화 2300
     '이제 완전히 밤이네요. 오늘은 평소에 못 했던 취미 생활에 도전해보시는 건 어떠신가요? 전 요새 그림에 도전하고 있어요! 언젠가 금손 작가님 유설레가 되는 날까지, 열심히 노력하려고요!'
    ], # 수요일
    [# 화 2300 ~ 수 0030
     '벌써 한 주의 절반이 지나가고 있어요! 오늘 하루도 수고하셨어요! 안녕히 주무세요!',
     # 수 0630 ~ 수 0800
     '좋은 아침이에요! 벌써 한 주의 절반, 수요일이에요! 오늘도 푸른 하늘을 보면서 설빈레피딕스 열차를 타고 기분 좋게, 상쾌하게 시작해요!',
     # 수 0900 ~ 수 1100
     '오늘도 하늘민국의 하늘은 맑아요! 하늘민국의 \'하늘\' 부분의 어원은 2011년 당시 하토의 닉네임(\'하늘\'토끼)에서 따온 것이지만, 일각에서는 매일 하늘이 맑아서 하늘민국이라는 말이 있을 정도에요.',
     # 수 1100 ~ 수 1300
     '벌써 점심시간이 찾아왔어요! 설빈레피딕스의 구내식당은 수요일에는 수다날(\'수\'요일은 \'다\' 먹는 \'날\')이라면서 한 그릇 음식이 주로 나오는데, 서지은승무본부를 제외하면 대부분 맛있는 것 같아요!',
     # 수 1300 ~ 수 1430
     '점심은 맛있게 드셨나요? 한 그릇 음식은 맛도 있고 빨리 먹을 수 있어서 좋은 것 같아요! 특히 저 같은 승무 직렬은 점심 시간이 따로 없어서 비는 시간에 점심을 먹어야 해서 더더욱이요.',
     # 수 1430 ~ 수 1630
     '혹시 교보문고eBook 수요캐시 받으셨나요? 4시까지 받으실 수 있어요! 저는 매주 수요일마다 수요캐시를 받아서 재미있는 라노벨과 만화를 사는 데 쓰고 있어요. 여러분도 한 번 받아보시는 건 어떠신가요?',
     # 수 1800 ~ 수 1930
     '오늘도 수고하셨어요! 벌써 한 주의 절반이 지나갔어요! 빠른 설빈레피딕스 열차를 타고 빛의 속도로 퇴근해요!',
     # 수 1930 ~ 수 2100
     '해가 지는 걸 보면 \'너는 나의 후회\' 2권의 한 장면이 떠올라요. \'수염을 깎다, 그리고 여고생을 줍다\'를 쓰신 시메시바님의 작품이에요. 여러분도 한 번 읽어보시는 게 어떠신가요?',
     # 수 2100 ~ 수 2300
     '이제 완전히 밤이네요. 오늘은 자기 계발에 도전하려고 해요! 물론 전차로 Go나 OpenBVE를 하는 것 뿐이지만요.'
    ], # 목요일
    [# 수 2300 ~ 목 0030
     '한 주의 반이 지났어요! 내일 하루만 버티면 불금이에요! 오늘 하루도 수고하셨어요! 안녕히 주무세요!',
     # 목 0630 ~ 목 0800
     '좋은 아침이에요! 벌써 목요일이에요! 상쾌하고 선선한 바람이 불어오는 게 기분 좋은 것 같아요. 오늘 하루도 설빈레피딕스 열차를 타고 기분 좋게, 상쾌하게 시작해요!',
     # 목 0900 ~ 목 1100
     '오늘도 하늘민국의 하늘은 높고 파래요! 거의 매일 가을 같은 날씨만 계속되어서 살기 좋은 것 같아요.',
     # 목 1100 ~ 목 1300
     '벌써 점심시간이에요! 오늘은 글로벌 데이라면서 구내식당에서 여러 나라의 가정식이 나오는 날이에요! 어느 나라의 음식이 나올까요? 개인적으로는 일식이었으면 좋겠어요!',
     # 목 1300 ~ 목 1430
     '점심은 맛있게 드셨나요? 다른 나라의 가정식은 대부분 맛있는 것 같아요! 오후에도 힘내서 열심히 일해봐요!',
     # 목 1430 ~ 목 1630
     '슬슬 나른해지는 시간이에요... 몰래 틈틈이 애니나 라노벨 같은 걸 보면서 버텨야겠어요.',
     # 목 1800 ~ 목 1930
     '오늘도 수고하셨어요! 벌써 내일이 불금이에요. 한 주가 끝나가고 있어요! 빠른 설빈레피딕스 열차를 타고 빛의 속도로 퇴근해요!',
     # 목 1930 ~ 목 2100
     '목요일은 자주 가는 치킨집이 지역 슈퍼마켓과 제휴해서 할인을 하는 날이에요! 치킨 값이 4천원 할인되는 데다가 3만원 이상 사면 만 원이 할인되는 슈퍼마켓 앱 쿠폰도 줘서 좋긴 한데... 살 찌니까 먹으면 안 되겠죠..?',
     # 목 2100 ~ 목 2300
     '오늘 하루도 완전히 끝나가고 있네요... 오늘은 평소 즐겨 하던 게임을 해 보려고 해요! 물론 일일 퀘스트만 겨우 돌고 끄겠지만요.'
    ], # 금요일
    [# 목 2300 ~ 금 0030
     '드디어 내일이 불금이에요! 불금을 제대로 불태우기 위해, 오늘은 일찍 주무세요! 안녕히 주무세요!',
     # 금 0630 ~ 금 0800
     '좋은 아침이에요! 드디어 금 같은 금요일이 찾아왔어요! 오늘도 빠른 설빈레피딕스 열차를 타고 직장까지 빛의 속도로 이동해봐요!',
     # 금 0900 ~ 금 1100
     '불금이에요! 오늘만 버티면 주말동안 놀거나 쉴 수 있으니까, 오늘은 모든 것을 불태워서 열심히 일해봐요! 오늘 야근을 하는 건 슬프잖아요?',
     # 금 1100 ~ 금 1300
     '슬슬 점심시간이에요! 몇 시간만 더 버티면 퇴근이에요! 그러면 이틀동안 일에서 해방되는 거에요! 벌써부터 신나는 것 같지 않으신가요?',
     # 금 1300 ~ 금 1430
     '점심은 맛있게 드셨나요? 일에서 해방되기까지 얼마 남지 않았으니까, 마지막까지 힘 내서 열심히 일해봐요!',
     # 금 1430 ~ 금 1630
     '식곤증이 찾아오고 있어요. 그치만 내일은 토요일이니까! 조는 건 내일 하기로 하죠!',
     # 금 1800 ~ 금 1930
     '불금이에요! 한 주 동안 수고하셨어요! 이제 주말동안 열심히 쉬거나 놀아봐요!',
     # 금 1930 ~ 금 2100
     '(유설레가 자리를 비웠습니다. 양서도 유신시 엔유구 강냥동 북해해안길 8구간 강냥해수욕장~혜슬철교 구간으로 가시면 신나서 산책로를 달리고 있는 유설레를 보실 수 있을 것 같습니다.)',
     # 금 2100 ~ 금 2300
     '산책로를 달리고 오니까 조금 많이 피곤하네요... 내일 열심히 놀아야 하니까 오늘은 일찍 자야겠어요.'
    ], # 토요일
    [# 금 2300 ~ 토 0030
     '드디어 주말이에요! 주말동안 불타기 위해서라도 오늘은 일찍 자야겠어요! 안녕히 주무세요!',
     # 토 0030 ~ 토 0200
     '아직도 안 주무시는 건가요? 제대로 놀기 위해선 제대로 주무셔야 해요! 얼른 주무세요!',
     # 토 0200 ~ 토 0630은 평일 공통 대사 사용 '''
     # 토 0630 ~ 토 0800
     '토요일의 아침 공기는 토요일이라서 더 선선하고 특별한 것 같아요! 안녕히 주무셨나요? 드디어 주말이 시작되었어요!',
     # 토 0800 ~ 토 0900
     '오늘은 신나게 놀 거에요! 타이밍아케이드센터에서 팝픈뮤직이나 비트스트림 아침 대여를 달리면서 몸을 풀고...\n그런 다음에는 발길 닿는 대로 돌아다닐 거에요! 새로운 경험을 하는 걸 좋아하거든요.',
     # 토 0900 ~ 토 1030
     '(유설레가 자리를 비웠습니다. 양서도 유신시 엔유구 혜슬동 타이밍아케이드센터 B2층 BeatStream 8번기체 앞으로 가시면 대여판과 함께 열심히 성과를 내고 있는 유설레를 보실 수 있을 것 같습니다. BeatStream은 2017년에 서비스가 종료되어서 모두 노스텔지어로 개조되지 않았냐고요? 하늘민국은 아직 BeatStream이 살아있는 세계관이라서요.)',
     # 토 1030 ~ 토 1130
     '오늘은 다행히 성과를 많이 냈어요! 그럼 이제 발길 닿는 대로 돌아다녀볼까요?',
     # 토 1130 ~ 토 1300
     '저는 승무 직렬이라 항상 열차를 운행하고 있지만, 이렇게 객실에 탄 채로 측면의 풍경을 바라보는 건 새로운 것 같아요.\n슬슬 점심시간이네요! 점심 맛있게 드세요!',
     # 토 1300 ~ 토 1415
     '점심은 맛있게 드셨나요? 저는 주변의 일본 가정식 가게에서 연어를 살짝 구운 사케동을 먹었어요! 진짜 연어는 너무 맛있는 것 같아요.',
     # 토 1415 ~ 토 1530
     '오늘도 하늘민국의 하늘은 구름 한 점 없이 높고 맑네요. 오늘은 산으로 갈까요, 바다로 갈까요?',
     # 토 1530 ~ 토 1645
     '바다가 눈 앞에 보이는 카페에서 틈틈이 끄적이던 장편소설을 쓰려고 태블릿을 켜고 앉았는데... 결국 애니를 보고 말았어요. 푸른 바다의 파도 소리를 들으면서 보는 애니는... 최고더라고요!',
     # 토 1645 ~ 토 1800
     '해수욕장으로 나왔어요. 모래의 감촉과 적당한 소음, 파도소리와 바닷물의 시원한 감촉, 끝이 보이지 않는 푸른 하늘과 에메랄드빛 바다가 어우러져 환상적인 풍경을 이루고 있어요!',
     # 토 1800 ~ 토 1930
     '슬슬 노을이 지는 걸 보니까 저녁을 먹을 시간인 것 같네요. 여러분은 무엇을 드실 건가요? 전 대패삼겹살을 먹으러 갈 거에요!',
     # 토 1930 ~ 토 2030
     '기분이 저기압일 땐 고기 앞으로 가라는 말이 맞는 것 같아요. 앞으로 1주일 동안 살아갈 동력을 얻었어요! 저녁은 맛있게 드셨나요?',
     # 토 2030 ~ 토 2200
     '오늘 하루도 끝나가고 있네요... 진짜 주말이 하루만 더 늘어났으면 좋겠어요. 주 4일만 출근하는 꿈의 직장은 존재하지 않는 걸까요?',
     # 토 2200 ~ 토 2330
     '슬슬 잘 준비를 해야 하는 시간이네요! 전 오늘 야간 운행이라 차량기지로 가고 있긴 하지만요. 미리 안녕히 주무세요!'
    ], # 일요일
    [# 토 2330 ~ 일 0030
     '야간 운행은 진짜 너무 졸린 것 같아요. 그렇지만 제가 실수하면 대규모의 인명사고로 이어지니까 정신 바짝 차려야 해요! 하암...',
     # 일 0030 ~ 일 0130
     '이제 오늘의 막차만 운행하면 잠시 쉴 수 있어요. 그래봤자 종착역까지 1시간 가까이 걸리지만요.\n아직도 안 주무시는 건가요? 주말 동안 충분히 주무시지 않으면 평일에 일하실 때 엄청 피곤해서 힘들어하실 거에요. 얼른 주무세요!',
     # 일 0130 ~ 일 0230
     '저는 겨우 막차까지의 운행을 마치고 승무본부의 숙소에 누웠어요. 이제 약 4시간 정도 쪽잠을 자고 내일 새벽 첫차부터 아침까지 운행해야 퇴근이에요.\n밤이 늦었어요. 밤을 새실 건가요? 평일 동안 엄청 힘들어하실 거에요. 지금 바로 폰이나 컴퓨터를 끄고 침대나 이부자리로 가서 누우세요!',
     # 일 0230 ~ 일 0500은 공통 대사 사용 '''
     # 일 0500 ~ 일 0630
     '좋은 아침..? 새벽..? 이에요! 이제 5시간 정도만 더 운행하면 퇴근이에요. 퇴근할 때 까지 열심히 일할게요!',
     # 일 0630 ~ 일 0800
     '좋은 아침이에요! 해안가를 달리는 노선의 열차를 운행하면서 보는 일출은 진짜 엄청 아름다워요. 그 아름다움에 홀려서 제한속도를 초과하거나 역을 통과해버리면 큰일이지만요.',
     # 일 0800 ~ 일 0900
     '일요일인데도 승객이 많네요. 놀러 온 분들이 많아서 그런 걸까요?',
     # 일 0900 ~ 일 1000
     '이제 퇴근하기 전 마지막으로 운행할 열차에 탔어요! 종착역까지 1시간 가까이 걸리긴 하지만, 힘을 내서 운행할게요!',
     # 일 1000 ~ 일 1100
     '퇴근이에요! 이제 집에 가서 느긋하게 쉴 거에요.',
     # 일 1100 ~ 일 1200
     '집으로 가는 광역급행버스를 타고 가다 보면 북해 바다가 보이는데, 너무 예쁜 것 같아요. 끝이 안 보이는 데다가 깊이도 가늠이 되지 않지만 투명하고 아름다운 에메랄드빛을 내고 있어서, 언젠간 멀리까지 나가보고 싶어요!',
     # 일 1200 ~ 일 1300
     '퇴근하니까 점심시간이 되었네요. 점심은... 비빔면으로 때울까 싶어요!',
     # 일 1300 ~ 일 1400
     '점심은 맛있게 드셨나요? 오후에는 무엇을 하실 예정인가요? 전 소파에 파묻혀서 라이트 노벨을 볼 거에요!',
     # 일 1400 ~ 일 1500
     '수요일에 수요캐시로 산 라이트 노벨을 다 읽어버렸어요... 오랫만에 게임이나 해 볼까 싶어요!',
     # 일 1500 ~ 일 1600
     '도데체 블루 아카이브의 총력전 5만 등 안에는 어떻게 들어가는 걸까요..? 더 많이 연구해봐야겠어요.',
     # 일 1600 ~ 일 1700
     '결국 라프텔을 켰어요. 진짜로 봇치 더 락과 최애의 아이는 세기의 걸작인 것 같아요!',
     # 일 1700 ~ 일 1800
     '열심히 쉬면서 놀다 보니까 저녁을 먹을 시간이 되었네요. 여러분은 무엇을 드실 예정인가요? 저는 간단하게 버터장조림비빔밥으로 때울 것 같아요.',
     # 일 1800 ~ 일 1900
     '버터장조림비빔밥은 만들기도 쉽고 맛도 꽤 괜찮은 것 같아요! 여러분도 한 번 만들어서 드셔 보세요!',
     # 일 1900 ~ 일 2000
     '저녁은 맛있게 드셨나요? 아쉽지만 슬슬 내일 출근할 준비를 해야 할 시간이에요. 이번 한 주도 파이팅이에요!',
     # 일 2000 ~ 일 2130
     '이번 주의 마지막 노을이 저버렸어요. 주말도 끝이네요... 저는 근무표 대로 출근해야 해서 평일과 주말의 구분이 거의 없긴 하지만요.',
     # 일 2130 ~ 일 2300
     '숙소에서 쪽잠밖에 못 자서 그런지 많이 피곤하네요... 오늘은 일찍 자야겠어요. 미리 안녕히 주무세요!\n혹시 주간 퀘스트는 전부 마치셨나요? 일요일 24시나 28시에 초기화되는 게임들이 많아요! 혹시 미처 못 끝낸 퀘스트가 있으시다면 꼭 끝내주세요!'
    ]
]

__공통대사__ = [ #평일
     # 0030 ~ 0200
     '엣, 이렇게 늦었는데 아직도 안 주무시는 건가요? 얼른 주무세요!', # 평일 공통대사
      # 0200 ~ 0630
     '저기... 밤이 늦었거든요..? 밤을 새실 건가요? 내일 엄청 피곤해하실 거에요. 지금 바로 폰이나 컴퓨터를 끄고 침대나 이부자리로 가서 누우세요!', # 평일, 주말 공통대사 (일요일은 0230 ~ 0500)
     # 0800 ~ 0900
     '출근 전쟁 중이신가요? 조금만 더 버티면 분명 금방 회사나 학교에 도착할 테니까, 조금만 더 힘 내 주세요!', # 평일 공통대사
     # 1630 ~ 1800
     '조금만 더 일하면 퇴근이에요! 마지막까지 힘내주세요!' # 평일 공통대사
]
    

class _시간(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    def 시간사담(self, now):
        # now 변수는 슬래시커맨드가 호출될 때 초기화되는 datetime 클래스를 그대로 상속시켜야 함 (이유 : tcode, weekcode 계산 방식 변경)
        tcode = __time__(now.hour, now.minute, now.second) # 시간 형식으로 변경
        weekcode = now.weekday() # 추후 dt 라이브러리를 구워삶아서 추가, 메세지를 월 6:30~금 18:00, 금 18:00~24:00, 토 00:00~24:00, 일 00:00~월 06:30으로 세분화하기
        # weekcode는 월요일이 0, 화요일이 1 ... 일요일이 6인 int형 값
        # tcode는 datetime.time형의 데이터
        if weekcode <= 4 : # 평일은 요일 별로 대사만 다를 뿐 대사가 달라지는 시간대는 똑같음, 그래서 일괄적으로 처리
            if __checkLess__(tcode, 0, 30): # 평일 0000~0030 요일별 대사
                return(__대사__[weekcode][0])
            elif __checkLess__(tcode, 2, 0): # 평일 0030~0200 공통 대사 : 엣, 이렇게 늦었는데 ~
                return(__공통대사__[0])
            elif __checkLess__(tcode, 6, 30): # 평일 0200~0630 공통 대사 : 저기... 밤이 늦었거든요..? ~
                return(__공통대사__[1])
            elif __checkLess__(tcode, 8, 0): # 평일 0630~0800 요일별 대사
                return(__대사__[weekcode][1])
            elif __checkLess__(tcode, 9, 0): # 평일 0800~0900 공통 대사 : 출근 전쟁 중이신가요? ~
                return(__공통대사__[2])
            elif __checkLess__(tcode, 11, 0): # 평일 0900~1100 요일별 대사
                return(__대사__[weekcode][2])
            elif __checkLess__(tcode, 13, 0): # 평일 1100~1300 요일별 대사
                return(__대사__[weekcode][3])
            elif __checkLess__(tcode, 14, 30): # 평일 1300~1430 요일별 대사
                return(__대사__[weekcode][4])
            elif __checkLess__(tcode, 16, 30): # 평일 1430~1630 요일별 대사
                return(__대사__[weekcode][5])
            elif __checkLess__(tcode, 18, 0): # 평일 1630~1800 공통 대사 : 조금만 더 일하면 퇴근이에요! ~
                return(__공통대사__[3])
            elif __checkLess__(tcode, 19, 30): # 평일 1800~1930 요일별 대사
                return(__대사__[weekcode][6])
            elif __checkLess__(tcode, 21, 0): # 평일 1930~2100 요일별 대사
                return(__대사__[weekcode][7])
            elif __checkLess__(tcode, 23, 0): # 평일 2100~2300 요일별 대사
                return(__대사__[weekcode][8])
            else:
                return(__대사__[weekcode+1][0]) # 평일 2300~0000, 다음날 맨 첫번째 대사 (전날 2300 ~ 당일 0030)
        elif weekcode == 5: # 토요일
            if __checkLess__(tcode, 0, 30):
                return(__대사__[weekcode][0])
            elif __checkLess__(tcode, 2, 0):
                return(__대사__[weekcode][1])
            elif __checkLess__(tcode, 6, 30):
                return(__공통대사__[1])
            elif __checkLess__(tcode, 8, 0):
                return(__대사__[weekcode][2])
            elif __checkLess__(tcode, 9, 0):
                return(__대사__[weekcode][3])
            elif __checkLess__(tcode, 10, 30):
                return(__대사__[weekcode][4])
            elif __checkLess__(tcode, 11, 30):
                return(__대사__[weekcode][5])
            elif __checkLess__(tcode, 13, 0):
                return(__대사__[weekcode][6])
            elif __checkLess__(tcode, 14, 15):
                return(__대사__[weekcode][7])
            elif __checkLess__(tcode, 15, 30):
                return(__대사__[weekcode][8])
            elif __checkLess__(tcode, 16, 45):
                return(__대사__[weekcode][9])
            elif __checkLess__(tcode, 18, 0):
                return(__대사__[weekcode][10])
            elif __checkLess__(tcode, 19, 30):
                return(__대사__[weekcode][11])
            elif __checkLess__(tcode, 20, 30):
                return(__대사__[weekcode][12])
            elif __checkLess__(tcode, 22, 0):
                return(__대사__[weekcode][13])
            elif __checkLess__(tcode, 23, 30):
                return(__대사__[weekcode][14])
            else:
                return(__대사__[weekcode+1][0]) # 23시 30분 이후로는 다음날 맨 첫 번째 대사를 불러옴
        elif weekcode == 6: # 일요일
            if __checkLess__(tcode, 0, 30):
                return(__대사__[weekcode][0])
            elif __checkLess__(tcode, 1, 30):
                return(__대사__[weekcode][1])
            elif __checkLess__(tcode, 2, 30):
                return(__대사__[weekcode][2])
            elif __checkLess__(tcode, 5, 0):
                return(__공통대사__[1])
            elif __checkLess__(tcode, 6, 30):
                return(__대사__[weekcode][3])
            elif __checkLess__(tcode, 8, 0):
                return(__대사__[weekcode][4])
            elif __checkLess__(tcode, 9, 0):
                return(__대사__[weekcode][5])
            elif __checkLess__(tcode, 10, 0):
                return(__대사__[weekcode][6])
            elif __checkLess__(tcode, 11, 0):
                return(__대사__[weekcode][7])
            elif __checkLess__(tcode, 12, 0):
                return(__대사__[weekcode][8])
            elif __checkLess__(tcode, 13, 0):
                return(__대사__[weekcode][9])
            elif __checkLess__(tcode, 14, 0):
                return(__대사__[weekcode][10])
            elif __checkLess__(tcode, 15, 0):
                return(__대사__[weekcode][11])
            elif __checkLess__(tcode, 16, 0):
                return(__대사__[weekcode][12])
            elif __checkLess__(tcode, 17, 0):
                return(__대사__[weekcode][13])
            elif __checkLess__(tcode, 18, 0):
                return(__대사__[weekcode][14])
            elif __checkLess__(tcode, 19, 0):
                return(__대사__[weekcode][15])
            elif __checkLess__(tcode, 20, 0):
                return(__대사__[weekcode][16])
            elif __checkLess__(tcode, 21, 30):
                return(__대사__[weekcode][17])
            elif __checkLess__(tcode, 23, 0):
                return(__대사__[weekcode][18])
            else:
                return(__대사__[0][0]) #월요일 맨 첫 번째 대사를 불러옴, weekcode가 바뀌면 이 부분 필히 수정해야 함
        else:
            return('weekcode를 잘못 불러왔어요! 처리 중 0시 0분이 지났거나 자료형 관련 문제로 인한 일시적일 오류일 가능성이 크니까 다시 한 번 시도해 주세요!')
            # 아마 주로 이 예외가 뜨는 경우는 weekcode가 7이 뜨는 상황일 것임
        '''
        if(tcode <= __time__(0,30) or tcode > time(23)):
            return('슬슬 잘 준비를 해야 할 시간이네요! 저는 오늘 야간 운행이라 못 자지만요. 하암...')
        elif(tcode > __time__(0,30) and tcode <= __time__(6,30)):
            return('엣, 이렇게 늦었는데 아직도 안 주무시고 계신가요? 얼른 주무세요!')
        elif(tcode > __time__(6,30) and tcode <= __time__(9)):
            return('좋은 아침이에요! 오늘 하루도 설빈레피딕스 열차를 타고 기분 좋게, 상쾌하게 시작해요!')
        elif(tcode > __time__(9) and tcode <= __time__(11)):
            return('하늘이 참 맑죠? 하늘민국은 강수량이 적고 그마저도 겨울에 폭설로 내리는 게 대부분이라 이렇게 맨날 하늘이 파랗고 맑아요. 이 푸른 하늘을 보면서, 힘내서 열심히 일해요!')
        elif(tcode > __time__(11) and tcode <= __time__(13)):
            return('슬슬 점심시간이네요. 배고파요...')
        elif(tcode > __time__(13) and tcode <= __time__(16)):
            return('점심은 맛있게 드셨나요? 배가 불러서 졸리겠지만 같이 힘내요!')
        elif(tcode > __time__(16) and tcode <= __time__(18)):
            return('조금만 더 일하면 퇴근이에요. 화이팅이에요!')
        elif(tcode > __time__(18) and tcode <= __time__(21)):
            return('해도 졌겠다, 가벼운 산책 어때요? 전 비번인 날에는 매일 저녁 먹고 나와서 북해 해안가 산책로를 산책해요. 바닷바람도 상쾌하고 기분이 좋거든요.\n아, 그리고 신종 코로나 바이러스 때문에 수도권은 21시 이후로는 아무것도 못 한다면서요? 뭔가 일이 있으면 빨리 나가는 게 좋을 것 같아요.')
        elif(tcode > __time__(21) and tcode <= __time__(23)):
            return('이제 완전히 밤이네요. 이 시간에는 평소에 하지 못 했던 취미생활을 해 보는 게 어떨까요?')
        else:
            return('오류가 발생해 사담을 처리하지 못했어요. 명령어를 처리하는 도중에 각 시 n9분 59초가 지나면 드물게 발생할 수 있는 오류니까, 다시 한 번 시도해주세요!')
        '''
    
    @commands.slash_command(name='시간',guild_ids=guild_ids,description='현재 시간을 간단한 사담을 덧붙여서 알려줘요!')
    async def 시간(self,ctx):
        now = dt.now(tz(td(hours=9)))
        embed = discord.Embed(title=f'삐, 삐, 삐! 당신의 설레임과 함께, 설빈레피딕스에서\n{str(now.strftime("%Y년 %m월 %d일 %H시 %M분 %S.%f"))[:-3]}초를 알려드립니다!',description=self.시간사담(now),color=0xccffff)
        await ctx.respond(embed=embed)
        # await ctx.respond('삐, 삐, 삐! 당신의 설레임과 함께, 설빈레피딕스에서 {0:04d}년 {1:02d}월 {2:02d}일 {3:02d}시 {4:02d}분 {5:02d}.{6:03d}초를 알려드립니다.\n{7}\n이 사담은 2020년 9월 경 설레봇을 \'신 교통동호인 채팅방\'에서 돌릴 때 작성되었어요. 하늘토끼의 가상국가/가상철도 세계관과 관련되어 있거나 지금과는 맞지 않는 내용이 있을 수 있으니 양해 부탁드려요!'.format(now.year, now.month, now.day, now.hour, now.minute, now.second, int(now.microsecond/1000),self.시간사담(now)))

def setup(bot):
    bot.add_cog(_시간(bot))
