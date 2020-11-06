import csv

c.data = {
    "Essential,red": """
    Inoreader, https://jp.inoreader.com/folder/Article%20Update
    Google Scholar, https://scholar.google.co.jp
    Google News, https://news.google.com
    Overleaf, https://www.overleaf.com
    Wolfram|Alpha, https://www.wolframalpha.com
    Forvo, https://forvo.com
    Slite (LAB), https://qspin-ut.slite.com/app/root
    Slite (HOME), https://marui-family.slite.com/app/root
    マイナビ2022, https://job.mynavi.jp/2022
    リクナビ2022, https://job.rikunabi.com/2022
    健康管理報告サイト, https://www.u-tokyo.ac.jp/ja/general/healthcheck.html
    """,
    "University,blue": """
    UTREE, http://tokyo.summon.serialssolutions.com/#!/
    交流活動の概要 | 留学生支援ウェブサイト, https://www.u-tokyo.ac.jp/adm/inbound/ja/life-interact-ac.html
    UTokyo OPAC, https://opac.dl.itc.u-tokyo.ac.jp/opac/opac_search/
    東大生協 在庫検索/和書発注, https://www.coopbooknavi.jp/zaik/book_search.php
    大学生協 書籍, http://honya.univ.coop/
    東大 理学系研究科物理学専攻, http://www.phys.s.u-tokyo.ac.jp/
    UT-mate, http://www.c.u-tokyo.ac.jp/graduate/index.html
    ITC-LMS, https://itc-lms.ecc.u-tokyo.ac.jp/portal/login
    理学系研究科 端末管理システム, https://dhcp.adm.s.u-tokyo.ac.jp/auth/
    情報システムチーム, http://jimubu.adm.s.u-tokyo.ac.jp/public/index.php/%E6%83%85%E5%A0%B1%E3%82%B7%E3%82%B9%E3%83%86%E3%83%A0%E3%83%81%E3%83%BC%E3%83%A0
    UTokyo WiFi, http://www.u-tokyo.ac.jp/ja/administration/dics/service/wifi.html
    計算科学アライアンス, http://www.compsci-alliance.jp/
    御殿下記念館, http://www.undou-kai.com/goten/
    学外からデータベースや電子ジャーナルを使うには？, http://www.dl.itc.u-tokyo.ac.jp/gacos/faq/gakugai.html
    UTAS - the University of Tokyo, https://utas.adm.u-tokyo.ac.jp/campusweb/campusportal.do
    林研究室 | 量子スピントロニクス/フォトニクス, http://qspin.phys.s.u-tokyo.ac.jp/jp/index.html
    The University of Tokyo (東京大学) | 学生および教職員を対象したソフトウェアの割引, https://e5.onthehub.com/WebStore/ProductsByMajorVersionList.aspx?cmi_cs=1&cmi_mnuMain=f4b2ea63-9ba9-e511-9413-b8ca3a5db7a1&ws=5a131a7b-a30a-e811-80fe-000d3af41938&vsro=8
    スペシャル・イングリッシュ・レッスン, http://www.sel-ut.com/
    光物理学特論2019 - Ideguchi Group　井手口研究室, https://takuroideguchi.jimdo.com/lecture/%E5%85%89%E7%89%A9%E7%90%86%E5%AD%A6%E7%89%B9%E8%AB%962019/
    ‎www.issp.u-tokyo.ac.jp/public/optics/, http://www.issp.u-tokyo.ac.jp/public/optics/
    東京大学理学系研究科 TA/RA, https://thesis.phys.s.u-tokyo.ac.jp/tara/auth/login
    東京大学生協 書籍注文・検索システム, https://bookzaikonavi.jp/tokyo/html/
    """,
    "EC,green": """
    Amazon, https://www.amazon.co.jp
    アズワン, https://www.as-1.co.j
    MISUMI, https://jp.misumi-ec.com
    MonotaRO, https://www.monotaro.com
    ソーラボ, http://www.thorlabs.jp
    ASKUL, https://www.askul.co.jp
    ヨドバシ.com, https://www.yodobashi.com
    """,
    "Code,purple": """
    Github, https://github.com
    CircleCI, https://circleci.com/gh/y-marui
    teratail, https://teratail.com
    connpass, https://connpass.com
    CodeZine, https://codezine.jp
    mugendai, https://www.mugendai-web.jp
    Technology of DeNA, https://engineer.dena.jp
    Advances in Engineering, https://advanceseng.com
    COMPUTEX, https://www.computextaipei.jp
    CES, https://www.ces.tech
    CEATEC, https://www.ceatec.com
    IFA, https://www.ifa-berlin.com
    """,
    "Journals": """
    arXiv Analytics, http://arxitics.com
    Paperscape, http://paperscape.org
    Physical Review B, https://journals.aps.org/prb
    Physical Review Letters, https://journals.aps.org/prl
    Physical Review Applied, https://journals.aps.org/prapplied
    Physical Review A, https://journals.aps.org/pra
    Physical Review Research, https://journals.aps.org/prresearch
    Physical Review X, https://journals.aps.org/prx
    Reviews of Modern Physics, https://journals.aps.org/rmp
    Annual Review of Condensed Matter Physics, https://www.annualreviews.org/journal/conmatphys
    Applied Physics Letters, https://aip.scitation.org/journal/apl
    Journal of Applied Physics, https://aip.scitation.org/journal/jap
    Journal of Physics: Condensed Matter, https://iopscience.iop.org/journal/0953-8984
    Journal of Physics D: Applied Physics, https://iopscience.iop.org/journal/0022-3727
    Optics Express, https://www.osapublishing.org/oe/home.cfm
    Nano Letters, https://pubs.acs.org/journal/nalefd
    Nature, https://www.nature.com
    Nature Communications, https://www.nature.com/ncomms
    Nature Materials, https://www.nature.com/nmat
    Nature Nanotechnology, https://www.nature.com/nnano
    Nature Physics, https://www.nature.com/nphys
    Scientific Reports, https://www.nature.com/srep
    Science, https://www.sciencemag.org
    Science Advances, https://advances.sciencemag.org
    IEEE Xplore: IEEE Transactions on Magnetics, https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=20
    Annals of Physics, https://www.sciencedirect.com/journal/annals-of-physics
    Journal of Magnetism and Magnetic Materials, https://www.sciencedirect.com/journal/journal-of-magnetism-and-magnetic-materials
    Journal of Physics and Chemistry of Solids, https://www.sciencedirect.com/journal/journal-of-physics-and-chemistry-of-solids
    Physics Letters A, https://www.sciencedirect.com/journal/physics-letters-a
    Physics Letters B, https://www.sciencedirect.com/journal/physics-letters-b
    Physics Reports, https://www.sciencedirect.com/journal/physics-reports
    Journal of the Physical Society of Japan, https://journals.jps.jp/journal/jpsj
    """,
    "Publishers": """
    Maruzen eBook Library, https://elib.maruzen.co.jp/elib/html/Top?1
    eBook Collection, http://search.ebscohost.com/login.aspx?authtype=ip&group=main&profile=ehost&defaultdb=nlebk
    Springer, https://link.springer.com/search?facet-discipline=%22Physics%22&showAll=false&facet-content-type=%22Book%22
    O'Reilly Japan Ebook Store, https://www.oreilly.co.jp/ebook
    サイエンス社, http://www.saiensu.co.jp/?page=field_list&field_id=22&field_name=SGC
    IntechOpen, https://www.intechopen.com
    物性研究・電子版, http://www2.yukawa.kyoto-u.ac.jp/~bussei.kenkyu
    日本物理学会, https://member.jps.or.jp/a/member/mypageTop.do?act=show
    """,
    "Books": """
    CHEMISTRY OF BOOK, http://chemistrybook.blog.fc2.com/blog-entry-4.html
    Journal Club (TNTL), https://sites.google.com/site/hwllab/research/lab-meeting
    PDF : 物理の観点, http://blog.livedoor.jp/rikeidansi/tag/PDF
    rcmdBook.html, http://yoshinobu.issp.u-tokyo.ac.jp/rcmdbook.html
    超弦理論の勉強 : 大栗博司のブログ, https://planck.exblog.jp/15276375
    ファインマンの経路積分に入門しよう！, https://blog.goo.ne.jp/ktonegaw/e/0f47de5854daf4eb38339a73791544a8
    books, http://as2.c.u-tokyo.ac.jp/~shmz/books.html
    Book guide for physics, http://maya.phys.kyushu-u.ac.jp/~knomura/research/guide-phys/bookguide-phys.shtml.ja
    光のオンライン書店/TOPページ, http://shop.optronics.co.jp
    明倫館書店, https://www.meirinkanshoten.com
    四方堂書店, https://www.shi-ho-do.com
    読書メーター, https://bookmeter.com/home
    """,
    "KAKENHI": """
    科研費電子申請システム, https://www-kofu.jsps.go.jp/kofu1/shinsei/logon3.do
    科研費電子申請システム, https://www-kaken.jsps.go.jp/kaken1/tokushorei/logonCheck.do
    採用手続ポータルサイト, https://area31.smp.ne.jp/area/p/lalj9lbmjl1lisbt9/AI4p9F/login.html
    JSPS 電子申請システム, https://www-yousei.jsps.go.jp/yousei1/shinsei/index.html
    """,
    "E-Learning": """
    Open Culture, http://www.openculture.com
    Pythonプログラミング入門, https://sites.google.com/view/ut-python/%E3%83%9B%E3%83%BC%E3%83%A0?authuser=0
    東京大学 松尾研究室, https://weblab.t.u-tokyo.ac.jp
    Udemy, https://www.udemy.com
    intee, https://intee.jp/student/?for=eng
    言語処理100本ノック 2015, http://www.cl.ecei.tohoku.ac.jp/nlp100/#
    Chainer チュートリアル, https://tutorials.chainer.org/ja/tutorial.html
    Progate, https://prog-8.com/users/sign_in
    Grow with Google, https://grow.google/intl/ALL_jp
    paiza, https://paiza.jp/student/mypage
    Hackr.io, https://hackr.io
    コンピュータアーキテクチャ, https://news.mynavi.jp/series/computer_architecture
    Coursera, https://www.coursera.org
    edX, https://www.edx.org
    """,
    "Utility": """
    クロネコメンバーズ, https://cmypage.kuronekoyamato.co.jp/portal/entrance
    iShed, http://www7a.biglobe.ne.jp/~sohma/
    Dynamic Wallpaper Club, https://dynamicwallpaper.club/gallery
    Kamisora - Wallpaper Abyss, https://wall.alphacoders.com/by_creator.php?id=123043
    使い捨てメールアドレス, http://sute.jp/
    Moke_Meas - Dropbox, https://www.dropbox.com/developers/apps/info/n8gu7v2de9ujljb
    日経テレコン21, http://t21ipau.nikkei.co.jp/ipauth/auth/auth?sid=1
    テンプレート　ダウンロード | デジタルペーパー | デジタルペーパー | ソニー, https://www.sony.jp/digital-paper/support/template/
    ゆうびんマイページ | 日本郵便株式会社, https://yu-bin.jp/mypage/
    """,
    "Cloud Sourcing": """
    ランサーズ, https://www.lancers.jp
    クラウドワークス, https://crowdworks.jp
    ココナラ, https://coconala.com
    SUZURI, https://suzuri.jp
    """,
    "Cooking": """
    dancyu, https://dancyu.jp/recipe/index.html
    ノヴァのおすすめレシピ, https://www.nova-organic.co.jp/recipe
    男子ごはんのレシピ, https://www.osarai-kitchen.com/category/テレビ東京/男子ごはん
    """
}

for k, v in c.data.items():
    if isinstance(v, str):
        r = csv.reader(v.strip().split("\n"), delimiter=",")
        c.data[k] = [[title, url] for title, url, *_ in r]
