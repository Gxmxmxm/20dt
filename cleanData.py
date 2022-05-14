from fuzzy_que import fuzz

data = {
    '2022年，是中国共产党统一战线政策提出____周年。': ['100'],

    '中国共产党____决定与其他政党建立“民主的联合战线”。': ['二大'],

    '中国共产党____第一次明确提出无产阶级在民主革命中的领导权和工农联盟问题。': ['四大'],

    '1930年10月，各左翼文化团体组成____，这是文化界的统一战线组织。': ['中国左翼文化总同盟'],

    '1935年8月，中国共产党的____强调了建立包括上层在内的统一战线，扩大了抗日统一战线的范围。': ['《为抗日救国告全体同胞书》'],

    '1948年4月30日，中国共产党发出“纪念____口号”，号召各民主党派、各人民团体及社会贤达迅速召开政治协商会议，讨论并实现召集人民代表大会，成立民主联合政权。': ['‘五一’劳动节'],

    '毛泽东在____上强调要从关门主义中解放出来，建立广泛的抗日民族统一战线。': ['瓦窑堡会议'],

    '为适应建立抗日民族统一战线的要求，____将“工农共和国”改为“人民共和国”。': ['《中央关于目前政治形势与党的任务决议》'],

    '1936年4月，中共中央发表____，首次公开把国民党列入抗日统一战线的对象。': ['《为创立全国各党各派的抗日人民阵线宣言》', '《目前抗日统一战线中的策略问题》'],

    '1939年10月，毛泽东在____指出“统一战线问题，武装斗争问题，党的建设问题，是我们党在中国革命中的三个基本问题”。': ['《<共产党人>发刊词》'],

    '周恩来在____中强调，要建立一个巩固的新民主主义的统一战线，就是要认清敌人、队伍和司令官这三个问题。': ['《论统一战线》'],

    '重庆谈判期间，毛泽东邀请许德珩、梁希、潘菽等人会谈，鼓励他们成立永久性的政治组织，促成了____的建立。': ['九三学社'],

    '1946年2月，民建、救国会、民联等民主党派联合其他团体组织举行陪都各界庆祝政协会议成功大会。国民党特务及暴徒捣毁会场，殴打民主人士及与会群众，制造了____事件。': ['较场口'],

    '1947年，毛泽东在____指出要组成民族统一战线，打倒蒋介石独裁政府，成立民主联合政府。': ['《目前形势和我们的任务》'],

    '1948年“五一口号”第____条号召：各民主党派、各人民团体、各社会贤达迅速召开政治协商会议，讨论并实现召集人民代表大会，成立民主联合政府。': ['五'],

    '1981年6月，中国共产党十一届六中全会通过的《关于建国以来党的若干历史问题的决议》中，对于新时期统一战线工作，明确指出了要巩固和扩大____。': ['爱国统一战线'],

    '1956年，毛泽东提出中国共产党要与民主党派实行“长期共存、互相监督”方针的重要讲话是____。': ['《论十大关系》'],

    '“西安事变”的发生时间是____。': ['1936年', '长期共存、互相监督、肝胆相照、荣辱与共'],

    '民族区域自治是中国共产党解决我国民族问题的一项基本国策。1984年，我国正式制定了《____》。': ['中华人民共和国民族区域自治法'],

    '1981年9月30日，全国人大常委会委员长____向新华社记者发表谈话，进一步阐明了对台工作九条方针，标志着“和平统一、一国两制”方针初步成型。': ['叶剑英'],

    '1983年4月，中央统战部召开了新中国成立以来第一次全国性统一战线____座谈会。': ['理论'],

    '“文革”结束后，标志着统一战线进入新的历史发展阶段的会议是____。': ['中国共产党十一届三中全会'],

    '统一战线最根本的问题是____。': ['领导权问题'],

    '统战工作的本质要求是____。': ['大团结大联合'],

    '中央统战工作会议强调，要坚持党委统一领导、统战部牵头协调、有关方面各负其责的____工作格局。': ['大统战'],

    '2007年，国务院新闻办公室发表____白皮书，第一次使用协商民主的概念。': ['《中国的政党制度》'],

    '《关于加强政党协商的实施意见》指出，无党派人士是政治协商的重要组成部分，参加____。': ['政党协商', '“对口帮扶”'],

    '积极引导宗教与社会主义社会相适应，一个重要任务就是支持我国宗教坚持____方向。': ['中国化'],

    '衡量中国的政治制度和政党制度，最根本的是要从____出发。': ['中国国情'],

    '习近平总书记在中央统战工作会议上指出，在港澳工作、对台工作、侨务工作中，要发挥统一战线____的作用。': ['争取人心'],

    '国家统一之基、民族团结之本、精神力量之魂是____。': ['中华民族共同体意识'],

    '我国社会主义民主政治的特有形式和独特优势是____。': ['协商民主'],

    '第三次中央新疆工作座谈会指出，____是新疆长治久安的重要基础。': ['发展'],

    '1994年4月，全国工商联提出以帮助“老、少、边、穷”地区开发资源、兴办企业、培训人才为主要内容的____。': ['光彩事业'],

    ' 中国侨联是由全国归侨、侨眷组成的____。': ['全国性人民团体'],

    '1992年，大陆海协会与台湾海基会就坚持一个中国原则的态度交换意见，达成____。': ['九二共识'],

    '第19次全国统战工作会议指出，我国社会的____是当代中国社会的重要特征，是统一战线存在和发展的客观基础。': ['一致性和多样性'],

    '做好新形势下统战工作，必须掌握规律、坚持原则、讲究方法，最根本的是要____。': ['坚持党的领导'],

    '习近平总书记在中央统战工作会议上指出，统战工作解决的是____问题。': ['人心和力量'],

    '在中国大陆范围内，除执政的中国共产党以外，还有____个民主党派。': ['8'],

    '民盟的全称是____。': ['中国民主同盟'],

    '中国民主建国会的成员以____人士为主。': ['经济界'],

    '九三学社最初是“民主科学座谈会”，后为纪念1945年9月3日____这一历史性日子，改称为九三学社。': ['抗日战争和世界反法西斯战争胜利', '56'],

    '我国省级建制的五个自治区是以____命名的。': ['回族、藏族、壮族、维吾尔族、蒙古族', '高度聚居'],

    '习近平总书记在党的十九大报告中强调：“全面贯彻党的民族政策，深化民族团结进步教育，铸牢中华民族共同体意识，加强各民族交往交流交融，促进各民族像____一样紧紧抱在一起，共同团结奋斗、共同繁荣发展。': ['石榴籽'],

    '____是实施《宪法》规定的民族区域自治制度的基本法律。': ['《民族区域自治法》'],

    '西安事变的和平解决标志着____。': ['抗日民族统一战线初步形成'],

    '中国民主党派中成立最早的是____。': ['中国致公党'],

    '党历来重视、关心党外知识分子，根据各个历史时期不同工作重心的需要制定和实施党外知识分子政策，大体上可以划分为四个时段和四个层次，概括为八个字，即____。': ['“争取、改造、培养、依靠”'],

    '____全国人大一次会议把“中国共产党领导的多党合作和政治协商制度将长期存在和发展”载入宪法。': ['八届'],

    '____全国人大一次会议把中国共产党领导的多党合作和政治协商制度将长期存在和发展载入宪法。  ': ['八届'],

    '____全国人大一次会议把中国共产党领导的多党合作和政治协商制度将长期存在和发展载入宪法。': ['八届'],

    '以下说法正确的是____。\n①统一战线工作任务重的党中央以及省、市两级党委派出机关设置统一战线工作机构\n②乡（镇、街道）党组织应当有人员负责统一战线工作\n③统一战线工作任务重的高等学校、科研院所党委设置统一战线工作机构': [
        '①②③'],

    '集体宗教活动应当由____主持。': ['宗教教职人员'],

    '习近平2017年3月4日看望参加全国政协十二届五次会议的民进、农工党、九三学社委员并参加联组会时强调，我国广大____要以时不我待的紧迫感、舍我其谁的责任感，主动担当积极作为，刻苦钻研，勤奋工作，为全面建成小康社会、建设世界科技强国作出更大贡献。': [
        '知识分子'],

    '习近平2017年3月4日看望参加全国政协十二届五次会议的民进、农工、九三学社委员并参加联组会时强调，我国广大____以时不我待的紧迫感、舍我其谁的责任感，主动担当积极作为，刻苦钻研，勤奋工作，为全面建成小康社会、建设世界科技强国作出更大贡献。': [
        '知识分子'],

    '1992年，大陆海协会与台湾海基会就坚持    的态度交换意见，达成九二共识。': ['一个中国原则'],

    '1992年，大陆海协会与台湾海基会就坚持____的态度交换意见，达成九二共识。': ['一个中国原则'],

    '党的十九大修改的《中国共产党党章》总纲中明确，“中国共产党维护和发展平等团结互助和谐的社会主义民族关系，积极培养、选拔少数民族干部，帮助少数民族和民族地区发展经济、文化和社会事业，____，实现各民族共同团结奋斗、共同繁荣发展”。': [
        '铸牢中华民族共同体意识'],

    '2014年9月，习近平总书记在中央民族工作会议讲话中强调：“用____来保障民族团结，增强各族群众法律意识”。': ['法律'],

    '____是做好民族工作的根本保证。': ['坚持党的领导'],

    '我国目前知识分子队伍中人数最多的群体是____。': ['党外知识分子'],

    '党外知识分子占知识分子总数的____。': ['75%'],

    '各级党委和政府是宗教工作的责任主体。____为本地区宗教工作的第一责任人。': ['党委主要负责人'],

    '我国宗教中，只有____是我国固有的，其它都是从国外传入的。': ['道教'],

    '《中国共产党统一战线工作条例》制定的根据是____。': ['《中国共产党章程》'],

    '统一战线工作对象是____。': ['党外人士', '民主党派成员'],

    '各地区各部门各单位统一战线工作第一责任人是____。': ['各级党委（党组）主要负责人'],

    '无党派人士的主体是____。': ['知识分子'],

    '民主党派的基本职能是____。': ['参政议政、民主监督、参加中国共产党领导的政治协商'],

    '党联系留学人员的桥梁纽带是____。': ['欧美同学会'],

    '非公有制经济领域统一战线工作方针是____。': ['信任、团结、服务、引导、教育'],

    '工商联履行职责的主题是____。': ['促进非公有制经济健康发展和非公有制经济人士健康成长'],

    '新的社会阶层人士统一战线工作思路是____。': ['信任尊重、团结引导、组织起来、发挥作用'],

    '统一战线人才教育培养的主阵地是____。': ['社会主义学院'],

    '参事室具备的性质有____。': ['统战性、咨询性'],

    '牵头协调党外代表人士管理工作的部门是____。': ['统战部'],

    '地方党委成立的统一战线工作领导小组组长由____担任。': ['同级党委书记'],

    '政党协商指的是____。': ['中国共产党同民主党派的政治协商'],

    '非公有制经济“两个健康”的内涵是____。': ['非公有制经济健康发展和非公有制经济人士健康成长'],

    '党外代表人士理论培训的重点是____。': ['政治培训'],

    '政协换届时，党外代表人士占政协委员的比例不低于____。': ['60%'],

    '大统战格局的内涵是____。': ['党委统一领导、统战部门牵头协调、有关方面各负其责'],

    '社会主义学院的指导和管理部门是____。': ['统战部'],

    '社会主义民族关系的本质特征是____。': ['平等团结互助和谐', '管'],

    '《中国共产党统一战线工作条例》正式印发的时间是____。': ['2020年12月21日'],

    '中央统一战线工作领导小组办公室设在____。': ['中央统战部'],

    '中国特色社会主义参政党建设的核心是____。': ['思想政治建设'],

    '统一战线是指中国共产党领导的、以工农联盟为基础的，包括全体社会主义劳动者、社会主义事业建设者、拥护社会主义爱国者、拥护祖国统一和____的联盟。': ['致力于中华民族伟大复兴的爱国者'],

    '以下说法正确的是____。': ['①②③'],

    '以下说法错误的是：____。': ['无党派人士不属于政治协商的重要组成部分'],

    '各级党委应当支持民主党派加强思想政治建设、组织建设、____、作风建设、制度建设，支持无党派人士加强自身建设。': ['履职能力建设'],

    '坚持广泛团结、____、积极引导、发挥作用的方针，做好出国和归国留学人员统一战线工作。': ['热情服务'],

    '在民族工作方面，全面深入持久开展马克思主义祖国观、民族观、____、历史观宣传教育。': ['文化观', '全面管理'],

    '对于新的社会阶层人士统一战线工作，要坚持信任尊重、____、组织起来、发挥作用的思路。': ['团结引导'],

    '海外统一战线工作的主要任务之一是：增进华侨和出国留学人员等对祖国的热爱和对中国共产党、____的理解认同。': ['中国特色社会主义', '①②③④⑤'],

    '坚持参事室统战性、咨询性和文史研究馆统战性、荣誉性的性质，党外参事、党外馆员不少于____。': ['70%'],

    '在民族工作方面，坚持和完善民族区域自治制度，深化____教育，促进各民族文化交流交融。': ['民族团结进步'],

    '各省（自治区、直辖市）、副省级城市和____可以成立党外知识分子联谊会。': ['省会城市'],

    '围绕促进民族团结、____，推动民族地区经济社会发展，不断满足各族群众的美好生活需要。': ['改善民生'],

    '在党外代表人士队伍建设上，发挥____作为统一战线人才教育培养主阵地作用。': ['社会主义学院', '坚持尊重、维护和照顾同盟者利益', '所有重点高校教授', '①②③④'],

    '促进宗教界人士和信教群众对伟大祖国、中华民族、____、中国共产党、中国特色社会主义的认同。': ['中华文化'],

    '推动构建亲清政商关系，形成有利于非公有制经济发展的政策环境、____、市场环境、社会环境。': ['法治环境'],

    '对台统一战线工作的主要任务不包括以下哪一项____。': ['实现两岸全面“三通”'],

    '各级人大代表候选人和各级政协委员中应当有适当数量的民营经济人士、____。': ['新的社会阶层人士'],

    '以下不属于党外代表人士的标准是____。': ['善于学习'],

    '____是统一战线最根本、最核心的问题。': ['坚持党的领导'],

    '港澳统一战线工作要全面准确贯彻____方针。': ['一国两制、港人治港、澳人治澳、高度自治'],

    '坚持和完善社会主义基本经济制度，制定、宣传和贯彻党关于发展____的方针政策。': ['非公有制经济', '会商会办制度'],

    '培育和发展中国特色商会组织，推动统一战线工作向商会组织有效____。': ['覆盖'],

    '《中国共产党统一战线工作条例》明确侨务工作的主要任务之一是：围绕凝心聚力同圆共享中国梦的主题，加强华侨、归侨、侨眷代表人士工作，____、____、____、____，为侨服务。': [
        '凝聚侨心、汇集侨智、发挥侨力、维护侨益'],

    '《中国共产党统一战线工作条例》明确海外统一战线工作的主要任务之一是：加强____，增进华侨和出国留学人员等对祖国的热爱和对中国共产党、中国特色社会主义的理解认同。': ['思想政治引领'],

    '根据《中国共产党统一战线工作条例》，省、市两级政府领导班子____配备党外干部。': ['应当'],

    '侨务工作的主要任务是：围绕____的主题，加强华侨、归侨、侨眷代表人士工作，凝聚侨心、汇集侨智、发挥侨力、维护侨益，为侨服务；统筹国内侨务和国外侨务工作，着力涵养侨务资源，引导华侨、归侨、侨眷致力于祖国现代化建设，维护和促进中国统一，实现中华民族伟大复兴，致力于增进中国人民与世界人民的友好合作交流，推动构建人类命运共同体。': [
        '凝心聚力同圆共享中国梦'],

    '保护华侨正当权利和利益，关心华侨的生存和发展，推动____建设，教育引导华侨遵守住在国法律，尊重当地文化习俗，更好融入主流社会，为住在国经济社会发展贡献智慧和力量，充分展现守法诚信、举止文明、关爱社会、团结和谐的大国侨民形象。': [
        '和谐侨社'],

    '保护归侨、侨眷合法权利和利益，____照顾归侨、侨眷特点，积极发挥他们与海外联系广泛的优势作用。': ['适当', '民主党派', '西藏', '限制', '二十周岁', '在国外加入了住在国国籍的华人'],

    '党的十一届三中全会后，随着改革开放政策的实施和社会主义市场经济发展，工人阶级、农民阶级和知识分子阶层出现了分化，并从中产生和发展起来一些____。': ['新的社会阶层'],

    '加强党对统一战线工作的集中统一领导，确保党在统一战线工作中总揽全局、协调各方，保证统一战线工作始终沿着正确的____前进。': ['政治方向'],

    '统一战线是指不同的____在一定的历史条件下，为了实现一定的共同目标，在某些共同利益的基础上组成的政治联盟。': ['社会政治力量'],

    '中国共产党在各个历史时期建立的统一战线，具体性质、目标、任务各有不同，但实现____始终是一个永恒的主题。': ['大团结、大联合', '民主统一战线'],

    '____是党委主管统战工作的职能部门。': ['统战部', '长期'],

    '巩固和发展我国社会主义政党关系，实现我国政党关系长期和谐，根本在于坚持走中国特色社会主义政治发展道路，关键在于____。': ['坚持和完善中国共产党领导的多党合作和政治协商制度'],

    '用____引领和教育宗教界人士和信教群众，支持和引导宗教界人士对宗教教义教规作出符合当代中国发展进步要求、符合中华优秀文化的阐释。': ['社会主义核心价值观'],

    '提高宗教工作法治化水平，善于用____规范宗教事务管理、调节涉及宗教的各种社会关系。': ['法律法规'],

    '统战部、____按照同级党委安排，参与民营企业党建工作。': ['工商联'],

    '港澳统一战线工作要全面准确贯彻____、____方针。': ['一国两制、港人治港、澳人治澳、高度自治'],

    '习近平总书记在中央统战工作会议上指出，在港澳工作、对台工作、侨务工作中，要发挥统一战线＿＿的作用。': ['争取人心'],

    '事实证明，____是解决历史遗留的香港、澳门问题的最佳方案，也是香港、澳门回归后保持长期繁荣稳定的最佳制度。': ['“一国两制”'],

    '省、市两级政府领导班子____配备党外干部。县级政府领导班子从实际出发____配备党外干部。': ['应当  积极'],

    '我国解决国内民族问题的基本政策和重要政治制度是____。': ['民族区域自治制度', '辩证唯物主义'],

    '坚持和完善社会主义基本经济制度，制定、宣传和贯彻党关于发展非公有制经济的方针政策，引导非公有制企业践行____理念。': ['新发展'],

    '中国共产党与各民主党派实行____监督。': ['互相'],

    '以下不是民主党派属性的是____。': ['中国特色社会主义议政党'],

    '《中国共产党统一战线工作条例》在____年12月21日发布施行。': ['2020'],

    '统一战线工作的原则之一，是坚持正确处理一致性和____关系。': ['多样性'],

    '统一战线工作对象为党外人士，重点是其中的____。': ['代表人士'],

    '统一战线工作对象为党外人士，重点是其中的____ 。': ['代表人士'],

    '共产党员应当团结信教群众，但____信仰宗教。': ['不得'],

    '党外代表人士队伍建设的培训工作要坚持____培训为主。': ['政治'],

    '党外代表人士队伍建设要加强____锻炼。': ['实践', '2'],

    '在党外代表人士队伍建设中，各级人大代表候选人和各级政协委员中应当有适当数量的____、新的社会阶层人士。': ['民营经济人士'],

    '统一战线是中国共产党凝聚人心____ 的政治优势和战略方针。': ['汇聚力量'],

    '统一战线工作的原则之一是坚持____的领导。': ['中国共产党'],

    '地方党委对本地区统一战线工作负____ 。': ['主体责任'],

    '各级党委（党组）主要负责人为本地区本部门本单位统一战线工作____。': ['第一责任人'],

    '地方党委成立统一战线工作领导小组，组长一般由____。': ['同级党委书记'],

    '高等学校党委统战部部长担任党委常委或者不设常委会的____。': ['党委委员'],

    '民主党派和无党派人士工作中，各级党委要为无党派人士履行职责提供必要____。': ['保障', '关注'],

    '最近一次中央统战工作会议是在____年召开。': ['2015'],

    '着眼促进____，做好非公有制经济领域统战工作。': ['“两个健康”'],

    '构建新型政商关系，关键是做到____。': ['“亲”“清”'],

    '为促进非公有制经济人士健康成长，中共中央统战部等部门定期举行全国非公有制经济人士____表彰大会。': ['优秀中国特色社会主义事业建设者'],

    '积极引导宗教与____相适应，一个重要的任务是支持我国宗教坚持中国化方向。': ['社会主义社会'],

    '党的十八大以来，在坚定推进两岸关系和平发展上，党和国家领导人倡导____理念。': ['“两岸一家亲”'],

    '____属性是人民政协最基本的属性。': ['统战'],

    '1956年，中国共产党以苏联为鉴戒，在处理党与非党关系方面首次提出“____”的方针。': ['长期共存，互相监督'],

    '1945年，____ 提出了“统一战线是一门专门科学”论断。': ['毛泽东', '“一个国家、两种制度”'],

    '1996年，正式成立了中国光彩事业____会。': ['促进'],

    '1997年，正式成立了中华海外____会。': ['联谊'],

    '2007年，国务院新闻办公室发表《中国的政党制度》____，全面介绍我国的政党制度。': ['白皮书'],

    '2005年3月，为反对和遏制“台独”分裂、促进祖国和平统一，十届全国人大三次会议高票通过了____。': ['《反国家分裂法》'],

    '准确把握宗教社会作用的____规律。': ['两重性'],

    '宗教工作本质上是____工作。': ['群众'],

    '宗教必须在____规定的权利和义务范围内活动。': ['宪法和法律'],

    '我国宪法第三十六条明确规定：“宗教团体和宗教事务不受____的支配。': ['外国势力'],

    '1937年7月8日，中共中央发出____，指出只有全民族实行抗战，才是中国的出路。': ['《为日军进攻卢沟桥通电》', '“清党”'],

    '经过重庆谈判，1945年10月，国共双方签署了____。': ['《政府与中共代表会谈纪要》'],

    '1947年2月，周恩来在中共中央政治局扩大会议上，提出蒋管区的人民运动是____。': ['“第二战场”'],

    '1947年，毛泽东作《目前形势和我们的任务》的报告，阐述了中国共产党关于____统一战线的方针和政策。': ['人民民主'],

    '1947年，毛泽东作《目前形势和我们的任务》，阐述了中国共产党关于____统一战线的方针和政策。': ['人民民主'],

    '1949年，中国共产党七届二中全会提出了党的工作重心由____转移到____。': ['乡村；城市'],

    '____年是中国共产党正式提出统一战线政策的100周年。': ['2022'],

    '1949年9月，中国人民政治协商会议第一届全体会议一致通过了《中国人民政治协商会议____》。': ['共同纲领'],

    '1950年，政务院在民族工作方面提出____方针。': ['慎重稳进'],

    '1956年10月，中央社会主义学院在北京创办，作为民主党派、无党派人士的“____ ”。': ['高级党校'],

    '1978年5月开始的____推动了统一战线思想解放。': ['真理标准大讨论', '邓小平'],

    '中国共产党三大的中心议题是讨论共产党员加入国民党的问题，明确规定党必须在____、____、____保持自己的独立性。': ['政治上', '思想上', '组织上'],

    '大革命时期统一战线的经验教训极其深刻，中国共产党为争取革命胜利，主张建立包括____、____、____、____在内的广泛的统一战线。没有统一战线，革命就不能发展并取得胜利。': ['工人', '农民',
                                                                                                 '民族资产阶级', '小资产阶级'],

    '红军长征经过十多个少数民族聚居区，明确规定____、____、____等针对少数民族上层的统一战线政策。': ['绝对不打彝民的土豪', '不打藏族土豪', '不立即提出没收土司的财产土地'],

    '1937年5月，中国共产党全国代表会议（当时称苏区代表会议）。会上，毛泽东先后作了____和____报告。': ['《中国共产党在抗日时期的任务》', '《为争取千百万群众进入抗日民族统一战线而斗争》'],

    '1938年7月，国民参政会第一次会议召开。毛泽东在《致国民参政会的贺电》中提出“最切”希望的三句话是____、____、____。': ['坚持抗战', '坚持统一战线', '坚持持久战'],

    '1941年3月，包括____、____、____、____、____及社会贤达在内的中国民主政团同盟在重庆秘密成立。': ['中国青年党', '国家社会党', '中华民族解放行动委员会', '中华职业教育社',
                                                                   '乡村建设协会'],

    '毛泽东指出____、____、____是中国共产党在中国革命中战胜敌人的三个法宝，三个主要的法宝。': ['统一战线', '武装斗争', '党的建设'],

    '抗日战争时期，在反对国民党顽固派的斗争中，中国共产党提出反摩擦斗争的____、____、____原则。': ['有理', '有利', '有节'],

    '1948年9月26日，中共中央决定将中央城市工作部改名为中央统一战线工作部，管理____、____、____、____、____等工作。': ['国民党统治区', '国内少数民族', '政权统战', '华侨',
                                                                             '各兄弟党的联络'],

    '新中国成立初期，宗教界提出的“三自”爱国运动是____、____、____。': ['自治', '自养', '自传'],

    '新时期统一战线两面旗帜是指____、____。': ['爱国主义', '社会主义'],

    '统一战线五大关系是指____、____、____、____、____。': ['政党关系', '民族关系', '宗教关系', '阶层关系', '海内外同胞关系'],

    '党外人士是中国共产党的____、____、____。': ['好参谋', '好帮手', '好同事'],

    '按照《中国共产党统一战线工作条例》规定，要“引导非公有制经济人士____、____、____、____、____、____，做合格的中国特色社会主义事业建设者”。': ['爱国', '敬业', '创新', '守法',
                                                                                          '诚信', '贡献'],

    '中央第七次西藏工作座谈会指出，做好西藏工作，必须坚持“____、____、____、____、____”的重要原则。': ['依法治藏', '富民兴藏', '长期建藏', '凝聚人心', '夯实基础'],

    '保持香港、澳门长期繁荣稳定，必须全面准确贯彻____、____、____、____的方针。': ['“一国两制”', '“港人治港”', '“澳人治澳”', '高度自治'],

    '党外知识分子工作，是统一战线的____、____工作。': ['基础性', '战略性'],

    '民主党派和无党派人士可通过____、____、____等方式，对中国共产党进行民主监督。': ['提出意见', '批评', '建议'],

    '中国共产党在新时期坚持和发展中国共产党领导下的多党合作的基本方针是____、____、____、____。': ['长期共存', '互相监督', '肝胆相照', '荣辱与共'],

    '加强各民族____、____、____，促进各民族像石榴籽一样紧紧抱在一起，共同团结奋斗、共同繁荣发展。': ['交融', '交流', '交往'],

    '宗教事务管理坚持____、____、____、____、____的原则。': ['保护合法', '制止非法', '遏制极端', '抵御渗透', '打击犯罪'],

    '我国宗教的特征是____、____、____、____、____。': ['长期性', '群众性', '民族性', '国际性', '复杂性'],

    '做好新时代宗教工作，需要构建____、____、____、____的宗教治理格局。': ['党委领导', '政府管理', '社会协同', '宗教自律'],

    '1940年3月，毛泽东为中共中央起草《抗日根据地的政权问题》的党内指示，明确指出，根据抗日民主统一战线政权的原则，在人员分配上，应规定为____、____、____各占三分之一，此即“三三制”政权建设思想。': [
        '共产党员', '非党的左派进步分子', '不左不右的中间派'],

    '“杂交稻之父”袁隆平是____、____。': ['无党派人士', '党外知识分子'],

    '出国和归国留学人士统一战线工作方针是____、____、____、____。': ['广泛团结', '热情服务', '积极引导', '发挥作用'],

    '《中国共产党统一战线工作条例》的指导思想是____、____、____、____、____。': ['马克思列宁主义', '毛泽东思想', '邓小平理论', '“三个代表”重要思想、科学发展观',
                                                       '习近平新时代中国特色社会主义思想'],

    '中国共产党统一战线工作的原则是____、____、____、____、____。': ['坚持中国共产党的领导；坚持高举爱国主义、社会主义旗帜', '坚持围绕中心、服务大局；坚持大团结大联合',
                                                 '坚持正确处理一致性和多样性关系', '坚持尊重、维护和照顾同盟者利益；坚持广交、深交党外朋友', '坚持大统战工作格局'],

    '中国共产党的统一战线工作的原则是____、____、____、____、____。': ['坚持中国共产党的领导；坚持高举爱国主义、社会主义旗帜', '坚持围绕中心、服务大局；坚持大团结大联合',
                                                  '坚持正确处理一致性和多样性关系', '坚持尊重、维护和照顾同盟者利益；坚持广交、深交党外朋友', '坚持大统战工作格局'],

    '各级统战部的主要职责是____、____、____、____、____、____。': ['了解情况', '掌握政策', '协调关系', '安排人事', '增进共识', '加强团结'],

    '政党协商的主要内容是____、____、____、____。': ['中国共产党全国和地方各级代表大会、党中央和地方各级党委有关重要文件的制定、修改',
                                       '宪法的修改建议，有关重要法律的制定、修改建议，有关重要地方性法规的制定、修改建议',
                                       '人大常委会、政府、政协领导班子成员和监察委员会主任、法院院长、检察院检察长建议人选', '关系统一战线和多党合作的重大问题'],

    '国家机关和国有企事业单位党外知识分子工作的重点对象是____、____、____、____。': ['具有高级职称的党外知识分子', '学术带头人或者重要业务骨干中的党外知识分子',
                                                       '担任国家机关、高等学校、科研院所、大中型国有企业中层以上领导职务的党外知识分子',
                                                       '其他有成就、有影响的党外知识分子'],

    '中国共产党的宗教工作基本方针是____、____、____、____。': ['全面贯彻党的宗教信仰自由政策', '依法管理宗教事务', '坚持独立自主自办原则', '积极引导宗教与社会主义社会相适应'],

    '宗教界对外交往的基础是____、____、____。': ['独立自主', '平等友好', '互相尊重'],

    '新的社会阶层人士主要包括____、____、____、____。': ['民营企业和外商投资企业管理技术人员', '中介组织和社会组织从业人员', '自由职业人员', '新媒体从业人员'],

    '新的社会阶层人士主要包括____ 、____ 、____ 、____。': ['民营企业和外商投资企业管理技术人员', '中介组织和社会组织从业人员', '自由职业人员', '新媒体从业人员'],

    '对台统一战线工作的主要任务是____、____、____、____、____。': ['贯彻执行党中央对台工作大政方针', '坚持一个中国原则，广泛团结海内外台湾同胞',
                                                '发展壮大台湾爱国统一力量，反对“台独”分裂活动', '不断推进祖国和平统一进程', '同心实现中华民族伟大复兴'],

    '海外统一战线工作的主要任务是____、____、____、____、____。': ['加强思想政治引领，增进华侨和出国留学人员等对祖国的热爱和对中国共产党、中国特色社会主义的理解认同',
                                                '传承和弘扬中华优秀文化，促进中外文化交流', '鼓励华侨参与我国改革开放和社会主义现代化建设，融入民族复兴伟业',
                                                '遏制“台独”等分裂势力，维护国家核心利益', '发挥促进中外友好的桥梁纽带作用，营造良好国际环境'],

    '海外统一战线工作的主要任务是____ 、____ 、____ 、____ 、____': ['加强思想政治引领，增进华侨和出国留学人员等对祖国的热爱和对中国共产党、中国特色社会主义的理解认同',
                                                   '传承和弘扬中华优秀文化，促进中外文化交流', '鼓励华侨参与我国改革开放和社会主义现代化建设，融入民族复兴伟业',
                                                   '遏制“台独”等分裂势力，维护国家核心利益', '发挥促进中外友好的桥梁纽带作用，营造良好国际环境'
                                                   ],

    '侨务工作的主要任务是____、____、____、____、____。': ['加强华侨、归侨、侨眷代表人士工作，凝聚侨心、汇集侨智、发挥侨力、维护侨益，为侨服务',
                                            '统筹国内侨务和国外侨务工作，着力涵养侨务资源，引导华侨、归侨、侨眷致力于祖国现代化建设', '维护和促进中国统一，实现中华民族伟大复兴',
                                            '致力于增进中国人民与世界人民的友好合作交流', '推动构建人类命运共同体'],

    '民主党派和无党派人士参政的主要内容包括____、____、____、____。': ['参加国家政权', '参与重要方针政策、重要领导人选的协商', '参与国家事务的管理', '参与国家方针政策、法律法规的制定和执行'],

    '民主党派自身建设的内容包括____、____、____、____、____。': ['思想政治建设', '组织建设', '履职能力建设', '作风建设', '制度建设'],

    '加强基层宗教工作要____、____、____、____、____。': ['建立健全县乡村三级宗教工作网络', '建立健全乡村两级责任制', '建立健全分级负责制度', '建立健全属地管理制度',
                                           '建立健全责任追究制度'],

    '工商联的基本特征是____、____、____。': ['统战性', '经济性', '民间性'],

    '加强对党外代表人士管理，重点了解掌握的重点是其____、____、____、____、____。': ['政治表现', '思想状况', '履行职责', '廉洁自律', '个人重要事项变化情况'],

    '在民族工作领域，要防范和打击各种____活动、____活动、____活动、____活动，维护国家统一、民族团结和社会稳定。': ['渗透颠覆破坏', '暴力恐怖', '民族分裂', '宗教极端'],

    '以下说法正确的有____、____、____、____。': ['坚定不移走中国特色解决民族问题的正确道路', '以铸牢中华民族共同体意识为主线', '坚持各民族一律平等', '全面贯彻党的民族政策'],

    '在党外代表人士队伍建设工作中，要发挥党外代表人士所在党派和团体____、____、____的作用。': ['自我管理', '自我教育', '自我监督'],

    '各级人大代表候选人和各级政协委员中应当有适当数量的____、____。': ['民营经济人士', '新的社会阶层人士'],

    '加强党的组织建设，树立和坚持正确选人用人导向，加强干部培养、交流和锻炼，打造____、____、____的统战干部队伍。': ['政治坚定', '业务精通', '作风过硬'],

    '解放战争期间，我们党通过在国民党军队中开展统战工作，充分展现了统一战线配合武装斗争取得的成就，具体为____、____、____、____。': [
        '促成国民党军队师以上重大起义60余起，起义兵力达114万，占国民党总兵力的1/7以上', '架机起义43架', '大小舰艇73艘', '地区性起义面积553万平方公里，占全国总面积的一半以上。'],

    '统战部是党委在统一战线工作方面的参谋机构、____、____、____。': ['组织协调机构', '具体执行机构', '督促检查机构'],

    '港澳统一战线工作的主要任务包括____、____、____、____。': ['全面准确贯彻“一国两制”“港人治港”“澳人治澳”、高度自治的方针', '坚持和完善“一国两制”制度体系', '支持港澳融入国家发展大局',
                                            '增强香港同胞、澳门同胞国家意识和爱国精神'],

    '在党外代表人士队伍建设方面，注意从国家机关、____、____以及____、____中发现党外代表人士。': ['国有企事业单位', '民营企业', '新的社会阶层人士', '出国和归国留学人员'],

    '无党派人士参政的主要内容是____、____、____、____。': ['参加国家政权', '参与重要方针政策、重要领导人选的协商', '参与国家事务的管理', '参与国家方针政策、法律法规的制定和执行'],

    '国家机关和国有企事业单位党组（党委）负责本单位党外知识分子工作，主要是____、____、____。': ['加强思想引导', '支持发挥作用', '组织党外知识分子参加统一战线工作和活动'],

    '统筹____和____工作，着力涵养____，引导华侨、归侨、侨眷致力于祖国____，维护和促进中国统一，实现中华民族伟大复兴，致力于增进中国人民与世界人民的友好合作交流，推动构建人类命运共同体，是侨务工作的一项主要任务。': [
        '国内侨务', '国外侨务', '侨务资源', '现代化建设'],

    '社会主义学院是____、____的联合党校。': ['民主党派', '无党派人士'],

    '加强党外代表人士培养要靠“两条腿”走路，指的是____、____。': ['一条是理论培训', '一条是实践锻炼'],

    '《中国共产党统一战线工作条例》在“统战部门自身建设”一章中，从____、____、____、____和纪律建设等方面对统战干部队伍建设提出要求。': ['政治建设', '思想建设', '组织建设', '作风建设'],

    '《中国共产党统一战线工作条例》规定，民族工作方面要“全面深入持久开展马克思主义____、____、____、____宣传教育，开展党的民族理论、政策学习宣传”。': ['祖国观', '民族观', '文化观',
                                                                                         '历史观'],

    '党的十九大报告指出，必须坚持和完善我国社会主义基本经济制度和分配制度，毫不动摇巩固和发展公有制经济，毫不动摇____、____、____非公有制经济发展。': ['鼓励', '支持', '引导'],

    '党的十九大报告指出，必须坚持和完善我国社会主义基本经济制度和分配制度，毫不动摇巩固和发展公有制经济，毫不动摇____、____ 、____非公有制经济发展。': ['鼓励', '支持', '引导'],

    '《中国共产党统一战线工作条例》规定，工商联对所属商会履行业务主管单位职责，对会员开展____、____，对所属商会主要负责人进行____。': ['思想政治工作', '教育培训', '考察考核'],

    '下列人员属于新的社会阶层人士中新媒体从业人员的是____。': ['新媒体出资人或出资代表人', '新媒体经营管理人员', '新媒体采编、技术研发人员'],

    '我国政党制度显著特征包括____。': ['共产党领导', '多党派合作', '共产党执政', '多党派参政'],

    '我国政党制度显著特征包括____、____、____、____。': ['共产党领导', '多党派合作', '共产党执政', '多党派参政'],

    '《中国共产党统一战线工作条例》在“党外代表人士队伍建设”一章中，规定了“建立健全组织部门、统战部门协作配合机制。在动议和讨论决定党外干部的____、____、____前，应当征求统战部门的意见”。': ['任免',
                                                                                                           '调动',
                                                                                                           '交流'],

    '《中国共产党统一战线工作条例》在“民主党派和无党派人士工作”一章中，规定了“党中央以及地方党委应当按照规定程序开展政党协商。支持民主党派和无党派人士参与____、____、____以及其他方面的协商。': ['人大协商',
                                                                                                             '政府协商',
                                                                                                             '政协协商'],

    '加强党的思想建设，用习近平新时代中国特色社会主义思想特别是习近平总书记关于加强和改进统一战线工作的重要思想____、____、____。': ['武装头脑', '指导实践', '推动工作'],

    '加强党的作风建设，坚决纠正“四风”，践行党的群众路线，教育、引导统战干部担当作为，加强同党外人士的团结联系，对党外人士____、____、____、____，做到诚恳谦和、平等待人、廉洁奉公。': ['待之以诚',
                                                                                                         '动之以情',
                                                                                                         '晓之以理',
                                                                                                         '助之以实'],

    '全面深入持久开展马克思主义祖国观、民族观、文化观、历史观宣传教育，开展党的民族理论、政策学习宣传，开展民族团结进步创建，增进各族群众对伟大祖国、____、____、____、____的认同。': ['中华民族',
                                                                                                        '中华文化',
                                                                                                        '中国共产党',
                                                                                                        '中国特色社会主义'],

    '巩固和发展平等团结互助和谐的社会主义民族关系，反对一切形式的____、____、____。': ['民族歧视', '大汉族主义', '地方民族主义'],

    '尊重和保护公民的____和____自由。': ['信仰宗教', '不信仰宗教'],

    '提高宗教工作法治化水平，运用____和____妥善处理宗教领域的矛盾和问题，教育引导宗教界人士和信教群众自觉维护宪法法律权威，在法律法规规定范围内开展活动。': ['法治思维', '法治方式'],

    '《中国共产党统一战线工作条例》规定，“加强党对统一战线工作的____领导，确保党在统一战线工作中____、____，保证统一战线工作始终沿着正确政治方向前进。': ['集中统一', '总揽全局', '协调各方'],

    '“三个离不开”的具体内容是____、____、____。这个观点高度概括和深刻阐述了中国各民族休戚相关、命运与共的血肉关系，对中国的民族团结进步事业有着重要的指导意义。': ['汉族离不开少数民族',
                                                                                             '少数民族离不开汉族',
                                                                                             '各少数民族之间也互相离不开'],

    '我国宗教关系包括____、____、____、____、____。': ['党和政府与宗教', '社会与宗教', '国内不同宗教', '我国宗教与外国宗教', '信教群众与不信教群众'],

    '尊重少数民族风俗习惯，包括____、____、____、____、____。': ['饮食习惯', '服饰习惯', '年节习惯', '婚姻习俗', '丧葬习俗'],

    '支持民主党派和无党派人士参与____、____、____以及其他方面的协商。': ['人大协商', '政府协商', '政协协商'],

    '构建党委统一领导、____、____的大统战工作格局。': ['统战部门牵头协调', '有关方面各负其责'],

    '地方党委领导同级____、____、____、____、法院、检察院和有关人民团体、企事业单位等做好本部门本单位本领域统一战线工作。': ['人大', '政府', '政协', '监察委员会'],

    '支持和鼓励宗教界在____、____、____的基础上开展对外交往。': ['独立自主', '平等友好', '互相尊重'],

    '党外代表人士队伍建设要坚持____为主，开展党外代表人士的____。发挥社会主义学院作为统一战线人才教育培养____。': ['政治培训', '理论培训', '主阵地作用'],

    '坚持参事室____、____和文史研究馆统战性、____的性质。': ['统战性', '咨询性', '荣誉性'],

    '民主党派参政的基本点是：____、____、____、____。': ['参加国家政权', '参与国家大政方针和国家领导人选的协商', '参与国家事务的管理', '参与国家方针、政策、法律、法规的制定执行'],

    '1990年，中共中央在《关于进一步加强和改进知识分子工作的通知》中指出，对知识分子要做到____、____、____。': ['政治上充分信任', '工作上放手使用', '生活上关心照顾'],

    '2015年中央统战工作会议上，习近平总书记围绕新的历史时期____、____、____进行了深入系统论述。': ['需要不需要统一战线', '需要什么样的统一战线', '如何巩固发展统一战线'],

    '根据《中国共产党统一战线工作条例》，符合条件的省级民主党派主委、工商联主席、无党派人士一般应当进入同级____、____、____领导班子。': ['人大常委会', '政府', '政协'],

    '根据《中国共产党统一战线工作条例》，统战部门要加强党的政治建设，教育引导统战干部____、____、____、____。': ['不忘初心、牢记使命', '增强“四个意识”', '坚定“四个自信”',
                                                                     '做到“两个维护”'],

    '根据《中国共产党统一战线工作条例》，各级法院、____领导班子应当配备____。高等学校领导班子中，符合条件的党外干部可以担任____。': ['检察院', '党外干部', '行政正职'],

    '根据《中国共产党统一战线工作条例》，统战部门会商有关部门，负责____、____、中的____的推荐提名工作。': ['人大代表', '人大常委会组成人员', '党外候选人'],

    '根据《中国共产党统一战线工作条例》，在宗教工作中要坚持政治上____、信仰上____，支持宗教团体加强自身建设和人才培养，巩固和发展党同宗教界的____。': ['团结合作', '互相尊重', '爱国统一战线'],

    '根据《中国共产党统一战线工作条例》，在宗教工作中要加强基层宗教工作，建立健全____、____、____三级宗教工作网络和乡（镇、街道）、村（社区）两级责任制。': ['县（市、区、旗）', '乡（镇、街道）',
                                                                                         '村（社区）'],

    '中国共产党和各民主党派实行____。中国共产党处于____和____地位，自觉接受民主党派的监督。': ['互相监督', '领导', '执政'],

    '统一战线工作对象的重点是____。': ['党外人士中的代表人士'],

    '根据《中华人民共和国归侨侨眷权益保护法》第二条规定，华侨是指____。': ['定居在国外的中国公民'],

    '坚持和发展____宗教理论，坚持我国宗教中国化方向，坚持以“导”的态度对待宗教，构建积极健康的宗教关系。': ['中国特色社会主义'],

    '以下人员不属于新的社会阶层的是____。': ['民营企业主要出资人'],

    '我国共有____个少数民族?': ['55'],

    '1981年，党的十一届六中全会通过《关于建国以来党的若干历史问题的决议》，其中把新时期统一战线正式定名为____ 。 ': ['爱国统一战线'],

    '毛泽东在中共七大上阐述了中国革命统一战线的问题，对全党提出____、____的要求。': ['“统一战线是一门专门科学”', '“我们要学会这一门科学”'],

    '我们有____、____ 、____挫败任何形式的“台独”分裂图谋。': ['坚定的意志', '充分的信心', '足够的能力'],

    '《关于中国公民确定民族成分的规定》：“不同民族的公民结合所生子女，或收养其他民族的幼儿，其民族成分在满十八周岁以前由父母或养父母商定，满十八周岁者由本人决定，年满____者不再更改民族成分。': ['二十周岁'],

    '建立健全____，了解反映非公有制经济人士诉求，帮助其依照法定程序维护合法权益。': ['政企沟通协商制度'],

    '我国对待宗教的正确态度是____。': ['导'],

    '工商联党组对所属商会党建工作履行____主体责任。': ['全面从严治党'],

    '中国共产党领导的多党合作和政治协商制度是我国的一项 ____   政治制度。': ['基本'],

    '中国共产党领导的多党合作和政治协商制度是我国的一项____政治制度。': ['基本'],

    '促进宗教人士和信教群众对____ 、____、____、____、中国特色社会主义的认同。': ["伟大祖国", "中华民族", "中华文化", "中国共产党"],

    '党外代表人士的基本标准是____、____、____。': ['政治坚定', '业绩突出', '群众认同'],

    '工商联是党领导的以民营企业和民营经济人士为主体的，具有____、____和____有机统一基本特征的人民团体和商会组织。': ['统战性', '经济性', '民间性'],

    '1940年7月，毛泽东在纪念抗战3周年所发表的____一文中，首次公开向全国人民提出了建立“三三制”政权的主张。': ['《团结到底》'],

    '我国世居少数民族分布最多的省份是____，共有25个世居少数民族。': ['云南'],

    '统一战线的重要法宝地位主要体现在____、____、____、____。': ['夺取革命、建设、改革事业胜利', '增强党的阶级基础、扩大党的群众基础、巩固党的执政地位', '全面建设社会主义现代化国家', '实现中华民族伟大复兴'],

    '2020年12月正式印发的《中国共产党统一战线工作条例》，是统一战线领域的基础主干____，是新时代统一战线的基本遵循。': ['党内法规'],

    '统战部门自身建设包括哪几个方面？': ['①②③④⑤'],







}


def findAns(title):
    # 精准匹配
    try:
        ansList = data[str(title).replace(" ", '')]
        return ansList
    except:
        # 精准匹配无果(报错)则测试模糊匹配
        return findAnsFuzz(title)



def findAnsFuzz(title):
    # 模糊匹配
    pro = {}
    for oo in data:
        like = fuzz.ratio(title, oo)  # 题目相似度
        # print(like)
        if like > 89:
            pro[like] = data[oo]    # {90: "答案1", 95: "答案2"}
    if len(pro) == 0:
        # print("模糊匹配失败，请联系管理员添加此题：", title)
        return []
    else:
        print(f"模糊匹配成功，相似度 {max(pro)}%")
        print(pro[max(pro)])
        return pro[max(pro)]    # 返回最具可性能的答案


if __name__ == '__main__':
    pass
    # print(len(data))
    # print(data['1956年，毛泽东提出中国共产党要与民主党派实行“长期共存、互相监督”方针的重要讲话是____'])
    a = findAnsFuzz('毛泽东在中共七大上阐述了中国革命统一，对全党提出____、____的要求')
    print(a)
    # aaa = {111:"21",33:"2",3311:"1"}
    # b = max(aaa)
    # print(b)
    # maxV = {}
    # print(len(maxV))