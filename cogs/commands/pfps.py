import discord
from discord.ext import commands
import random

pfpss = [
  'https://cdn.discordapp.com/attachments/608711473652563968/1018307916710817842/22EE8237-C6D8-4BDC-8366-596C4D6ED487.gif',
  'https://cdn.discordapp.com/attachments/608711478496854019/1018121440714817596/unknown.png',
  'https://cdn.discordapp.com/attachments/608711478496854019/1018051616756219916/5dc823c5bb21cdc63dac7dd86ec93d2f.jpg',
  'https://cdn.discordapp.com/attachments/608711476219478045/1019191077506396170/a_fe6fbe3cec2fccbff3c71ccb6d0c9f9a.gif',
  'https://cdn.discordapp.com/attachments/608711476219478045/1019186587180990514/a_4fbe6403d85f03bcd428ac52a04b1731.gif',
  'https://cdn.discordapp.com/attachments/608711476219478045/1018152608860475462/image5.gif',
  'https://cdn.discordapp.com/attachments/608711476219478045/1018152606893346816/Gif6.gif',
  'https://cdn.discordapp.com/attachments/608711476219478045/1018151757743923341/a_af347fce39d2a0640e672ffbad797a7a.gif',
  'https://cdn.discordapp.com/attachments/608711476219478045/1018151756221394944/a_62550197c4ec87e91770a22dd4f45edb-1.gif',
  'https://cdn.discordapp.com/attachments/608711476219478045/1018151755273474110/a_67d61390265cb7294137ab700b327755.gif',
  'https://cdn.discordapp.com/attachments/608711476219478045/1018151433671032892/a_44dcbf79100c201d91390c78e23fe39e.gif',
  'https://cdn.discordapp.com/attachments/608711476219478045/1018151432437899264/a_9e465caa99b2c136ecc6c98a8185c86f.gif',
  'https://cdn.discordapp.com/attachments/608711476219478045/1018151431276081202/a_6ea343b4bf2373d38adbc855877754de.gif',
  'https://cdn.discordapp.com/attachments/608711474952798221/1018984869424013333/ugur_askimin_ppsi.jpg',
  'https://cdn.discordapp.com/attachments/608711474952798221/1018949984843997214/e1240bba6622954599804b94eeea22b0.jpg',
  'https://cdn.discordapp.com/attachments/608711473652563968/1019152927220301875/ba90d567d37ae57d41c10ece156e2111.gif',
  'https://cdn.discordapp.com/attachments/608711473652563968/1018636127814570064/9de66e99de86f66cbe3d479ef6756e9b.gif',
  'https://cdn.discordapp.com/attachments/608711473652563968/1018309211983192184/147367F7-B146-4623-89D7-5E7FD3E633DA.gif',
  'https://cdn.discordapp.com/attachments/768864495522283560/1018984139946459196/IMG_20220912_233247.jpg',
  'https://cdn.discordapp.com/attachments/768864495522283560/1018983026589450270/2.png',
  'https://cdn.discordapp.com/attachments/768864495522283560/1018970085173497946/750f5e44205acea8ed30397cae020fa9.jpg',
  'https://cdn.discordapp.com/attachments/768864495522283560/1018955729496969317/a_85480d503d1c0bbe448742f4a2cd83a9.gif',
  'https://cdn.discordapp.com/attachments/768864615676903466/1019337978679668786/a_90a2caf6bd7be576a9ba3b4e4ba81810.gif',
  'https://cdn.discordapp.com/attachments/768864615676903466/1019336375293706392/menace-santana-menace-santana-gif.gif',
  'https://cdn.discordapp.com/attachments/768864615676903466/1019336312739856464/menace-santana-booskap.gif',
  'https://cdn.discordapp.com/attachments/768864615676903466/1019336014503874630/menace-santana.gif',
  'https://cdn.discordapp.com/attachments/768864615676903466/1019331930384248863/96ebadd862d6eeb5817c28b3472e2dc4.png',
  'https://cdn.discordapp.com/attachments/768864495522283560/1019357643141292042/b.gif',
  'https://cdn.discordapp.com/attachments/768864495522283560/1019341567066128435/013c579c700043c96583f99a0775ad6b.jpg',
  'https://cdn.discordapp.com/attachments/768864495522283560/1019328501154844733/pp_13.jpg',
  'https://cdn.discordapp.com/attachments/768864495522283560/1019311556800020500/a0133a1991742ed8e142af3f0c072563.png',
  'https://cdn.discordapp.com/attachments/768864495522283560/1019258155298992148/a_5eca60140eccaeec69f2662cbc600400.gif',
  'https://cdn.discordapp.com/attachments/768864495522283560/1019726853386272869/edfd38527129a09a90767ae23205ea73.jpg',
  'https://cdn.discordapp.com/attachments/768864495522283560/1019686929572315166/c62590c1756680060e7c38011cd704b5.jpg',
  'https://cdn.discordapp.com/attachments/768864495522283560/1019686282747719750/a_c2178733158e5e80a0ba80b10d53501a.gif'
]
boyspng = [
  'https://cdn.discordapp.com/attachments/608711478496854019/1018153780786774097/images_24.jpg',
  'https://cdn.discordapp.com/attachments/608711478496854019/1018153202975244379/98f0d329ea4452cbc51d45cde2601da2.jpg',
  'https://cdn.discordapp.com/attachments/608711478496854019/1018122035316150342/unknown.png',
  'https://cdn.discordapp.com/attachments/608711478496854019/1018121781036466226/unknown.png',
  'https://cdn.discordapp.com/attachments/608711478496854019/1018121729211629688/unknown.png',
  'https://cdn.discordapp.com/attachments/608711478496854019/1018121698165395566/unknown.png',
  'https://cdn.discordapp.com/attachments/608711478496854019/1018121684768788542/unknown.png',
  'https://cdn.discordapp.com/attachments/608711478496854019/1018121647074586654/unknown.png',
  'https://cdn.discordapp.com/attachments/608711478496854019/1018121647074586654/unknown.png',
  'https://cdn.discordapp.com/attachments/608711478496854019/1018121638778241084/unknown.png',
  'https://cdn.discordapp.com/attachments/608711478496854019/1018121620247814144/unknown.png',
  'https://cdn.discordapp.com/attachments/608711478496854019/1018121602254245908/unknown.png',
  'https://cdn.discordapp.com/attachments/608711478496854019/1018121572017508402/unknown.png',
  'https://cdn.discordapp.com/attachments/608711478496854019/1018121552568516652/unknown.png',
  'https://cdn.discordapp.com/attachments/608711478496854019/1018121536525324288/unknown.png',
  'https://cdn.discordapp.com/attachments/608711478496854019/1018121463422787625/unknown.png',
  'https://cdn.discordapp.com/attachments/608711478496854019/1018121448700772382/unknown.png',
  'https://cdn.discordapp.com/attachments/608711478496854019/1018051616756219916/5dc823c5bb21cdc63dac7dd86ec93d2f.jpg',
  'https://cdn.discordapp.com/attachments/608711478496854019/1018051616550703124/55f724042e6c9a8cffdf896a75835adf.jpg',
  'https://cdn.discordapp.com/attachments/608711478496854019/1018051616328396810/55981e6682c262aea523fcdada48e07d.jpg',
  'https://cdn.discordapp.com/attachments/608711478496854019/1019502062255484938/fc35beb42bd3d58546765fcbb37e9675.jpg',
  'https://cdn.discordapp.com/attachments/608711478496854019/1019502061802504192/aa623fb85df127a7d0788adb7afad424.jpg',
  'https://cdn.discordapp.com/attachments/608711478496854019/1019501988410572821/9879d6ae061333c7c3345ef01925a610.jpg',
  'https://cdn.discordapp.com/attachments/608711478496854019/1019501987877896232/15aeb18b8eb8c568ae465fc79d193de7.jpg'
]
boysgif = [
  'https://cdn.discordapp.com/attachments/608711476219478045/1018151755273474110/a_67d61390265cb7294137ab700b327755.gif',
  'https://cdn.discordapp.com/attachments/608711476219478045/1018151757743923341/a_af347fce39d2a0640e672ffbad797a7a.gif',
  'https://cdn.discordapp.com/attachments/608711476219478045/1019186587180990514/a_4fbe6403d85f03bcd428ac52a04b1731.gif',
  'https://cdn.discordapp.com/attachments/608711476219478045/1019190886602641438/a_440717d1a0682299b382721985e3ab44.gif',
  'https://cdn.discordapp.com/attachments/608711476219478045/1019190951064907847/a_580331609d1dbae6f8a924a5ccd1bc1a.gif',
  'https://cdn.discordapp.com/attachments/608711476219478045/1019191001824366592/a_9216e2285cf4662ec0278926521258e9.gif',
  'https://cdn.discordapp.com/attachments/608711476219478045/1019191048423100456/a_5629581e37281c6098d325673f40a75d.gif',
  'https://cdn.discordapp.com/attachments/608711476219478045/1019191077506396170/a_fe6fbe3cec2fccbff3c71ccb6d0c9f9a.gif',
  'https://cdn.discordapp.com/attachments/608711476219478045/1019191111085998110/a_81aa4b9a7bacd5d3937b7273be9ffbcd.gif',
  'https://cdn.discordapp.com/attachments/608711476219478045/1019191143545704528/a_5bc7210b892a6534e8a7c6a5b9a0a0d8.gif'
]
girlspng = [
  'https://cdn.discordapp.com/attachments/608711474952798221/1018949918427201628/9345e3b76b5b94b721b76139761717fd.jpg',
  'https://cdn.discordapp.com/attachments/608711474952798221/1018949978225397870/3e2efb2a9b7eb1d50acc80c68e64ae5c.jpg',
  'https://cdn.discordapp.com/attachments/608711474952798221/1018949984843997214/e1240bba6622954599804b94eeea22b0.jpg',
  'https://cdn.discordapp.com/attachments/608711474952798221/1018950006180425888/eac2545c5b7ca1bbad397dbcac43d028.jpg',
  'https://cdn.discordapp.com/attachments/608711474952798221/1018950018184519751/9ebe939f3206417bbb4fe213d562df76.jpg',
  'https://cdn.discordapp.com/attachments/608711474952798221/1018956823283367957/59a2920daca0e3ae08177c04dbebfa55.jpg',
  'https://cdn.discordapp.com/attachments/608711474952798221/1019006065653858404/e517461d37748604040875e98ce01672.jpg',
  'https://cdn.discordapp.com/attachments/608711474952798221/1019006067201556640/1a9c10217ec2dc1dbeb181990b48feaa.jpg',
  'https://cdn.discordapp.com/attachments/608711474952798221/1019006227210059789/7bad07723979d27368b992ff26454e4f.jpg',
  'https://cdn.discordapp.com/attachments/608711474952798221/1019006227210059789/7bad07723979d27368b992ff26454e4f.jpg',
  'https://cdn.discordapp.com/attachments/608711474952798221/1019025824785113180/bbdca2a3f44cf08cf6b861e5110ddece.jpg',
  'https://cdn.discordapp.com/attachments/608711474952798221/1019124254865887293/69a74536ca13732c665ca30be1d52c34.jpg',
  'https://cdn.discordapp.com/attachments/608711474952798221/1019124287711498290/6283ad38d48567fdead26f0f9ee196f6.jpg',
  'https://cdn.discordapp.com/attachments/608711474952798221/1019129050956042290/112e7c6c55f07c8f9b00d57827814bbd.jpg',
  'https://cdn.discordapp.com/attachments/608711474952798221/1019171107259023400/FWfy12hWYAIvYvr.jpg',
  'https://cdn.discordapp.com/attachments/608711474952798221/1019183142785007688/f146217a5975656d318f55a048c3d5be.jpg',
  'https://cdn.discordapp.com/attachments/608711474952798221/1019411261127135332/48456c2b6d46704eac62b74664f6adc3.webp',
  'https://cdn.discordapp.com/attachments/608711474952798221/1019411260628021248/f33b9743d7a51227a163b7d9f9761c2b.jpg',
  'https://cdn.discordapp.com/attachments/608711474952798221/1019398015330558012/817d8631e104efe01fc065ab287f7f23.jpg',
  'https://cdn.discordapp.com/attachments/608711474952798221/1019342233096433736/89ffa9f53a6ed48a47656c8024fe0ae6.jpg',
  'https://cdn.discordapp.com/attachments/608711474952798221/1019342220433817760/907b261b7e4a723fc205556c1e6feafe.jpg',
  'https://cdn.discordapp.com/attachments/608711474952798221/1019853188532289546/IMG_20220831_151223.jpg',
  'https://cdn.discordapp.com/attachments/608711474952798221/1019853120697815096/IMG_9719.png',
  'https://cdn.discordapp.com/attachments/608711474952798221/1019853073620930580/c1a45258e1af98f6677f7b53b7687f5e.jpg',
  'https://cdn.discordapp.com/attachments/608711474952798221/1019852824110182420/bdaffd216677d77faa74998bb96cb7ab.jpg',
  'https://cdn.discordapp.com/attachments/608711474952798221/1019852773803696159/unknown-9.png',
  'https://cdn.discordapp.com/attachments/608711474952798221/1019852761241755698/unknown-6_1.png',
  'https://cdn.discordapp.com/attachments/608711474952798221/1019852730916937788/4177d4499bd998d10a2b65c5acfec0a1.jpg',
  'https://cdn.discordapp.com/attachments/608711474952798221/1019852715184107540/3f1a8f1db321e3c5aa95d59ffe4a6942.jpg',
  'https://cdn.discordapp.com/attachments/608711474952798221/1019852686012715058/b436ab48c401575c1ee12e301eadae61.jpg',
  'https://cdn.discordapp.com/attachments/608711474952798221/1019852675237543946/8bae29fd38826f8045986a902de54add.jpg'
]
girlsgif = [
  'https://cdn.discordapp.com/attachments/608711473652563968/1018307916710817842/22EE8237-C6D8-4BDC-8366-596C4D6ED487.gif',
  'https://cdn.discordapp.com/attachments/608711473652563968/1018547736884293762/o.gif',
  'https://cdn.discordapp.com/attachments/608711473652563968/1018637183978053672/a_b9d30a968ff1829b0dc347b5c9231c3e.gif',
  'https://cdn.discordapp.com/attachments/608711473652563968/1018637429634257027/mavi_gif_25.gif',
  'https://cdn.discordapp.com/attachments/608711473652563968/1018637548886691850/IMG_6542.gif',
  'https://cdn.discordapp.com/attachments/608711473652563968/1019152978474717194/3667bfc33f7f271a59b4ae8ddba5ad61.gif',
  'https://cdn.discordapp.com/attachments/608711473652563968/1019153096804421632/0ba601f55a0bb68a17b5e3ad024b4d1f.gif',
  'https://cdn.discordapp.com/attachments/608711473652563968/1019153145319931944/7c68f7e7ccf6239e3f7aa9c9b9522499.gif',
  'https://cdn.discordapp.com/attachments/608711473652563968/1019153228740427796/2a407ae5981aa0f9a94da00045db00c0.gif',
  'https://cdn.discordapp.com/attachments/608711473652563968/1019181736204193802/1DFBB8CC-9783-42DB-BE8B-8C35027748A7.gif',
  'https://cdn.discordapp.com/attachments/608711473652563968/1019181736678133800/a_f07baf7e3c051e0af90bba08d6c0f574.gif',
  'https://cdn.discordapp.com/attachments/608711473652563968/1019182016568234034/hit_gif_14.gif',
  'https://cdn.discordapp.com/attachments/608711473652563968/1019182016220114944/gif_3_1-1.gif',
  'https://cdn.discordapp.com/attachments/608711473652563968/1019181740473974856/rererr.gif',
  'https://cdn.discordapp.com/attachments/608711473652563968/1019181740473974856/rererr.gif',
  'https://cdn.discordapp.com/attachments/608711473652563968/1019181739651899392/Man_PP_Gif_9.gif',
  'https://cdn.discordapp.com/attachments/608711473652563968/1019181738871754872/image0_17.gif',
  'https://cdn.discordapp.com/attachments/608711473652563968/1019324790747705395/a_5cf769c363a107c4f376484c0323a29b.gif',
  'https://cdn.discordapp.com/attachments/608711473652563968/1019299528668626954/a_f84900a162b4f54fc9bb6756251c80ea.gif',
  'https://cdn.discordapp.com/attachments/608711473652563968/1019299494321475594/a_c7fe0ca9b65247fc7ea4c6a5217a2393.gif',
  'https://cdn.discordapp.com/attachments/608711473652563968/1019299438184910948/a_70e031ccba3e1a91cb3da03c2183e497.gif',
  'https://cdn.discordapp.com/attachments/608711473652563968/1019603950049165343/edc6cbe81fd98982098de93a9253f42d.gif',
  'https://cdn.discordapp.com/attachments/608711473652563968/1019598841407885343/6.gif',
  'https://cdn.discordapp.com/attachments/608711473652563968/1019598840149594313/Rylie.gif',
  'https://cdn.discordapp.com/attachments/608711473652563968/1019598837926613032/2.gif',
  'https://cdn.discordapp.com/attachments/608711473652563968/1019581044804026388/a_cc0d2ae8230ee576c6e330e7f84ef3bb.gif',
  'https://cdn.discordapp.com/attachments/608711473652563968/1019603952561553448/9cc273b9196784a1b2d50eefd21c02c3.gif',
  'https://cdn.discordapp.com/attachments/608711473652563968/1019603951911456848/bbc721e2c8e48d79cd59da6824b1f861.gif',
  'https://cdn.discordapp.com/attachments/608711473652563968/1019603951559127111/7502e1ed0b08ff07e6c393e45575e51c.gif'
]
couplespng = [
  'https://cdn.discordapp.com/attachments/608711481969868811/1019199430353764412/20220913_125743.jpg',
  'https://cdn.discordapp.com/attachments/608711481969868811/1018526535881326633/unknown.png',
  'https://cdn.discordapp.com/attachments/608711481969868811/1018414869881557032/c46790afdfa2d8fc21c22368a0261307.jpg',
  'https://cdn.discordapp.com/attachments/608711481969868811/1018414869583773776/adcbdda4b721271e9dc01465415bd160.jpg',
  'https://cdn.discordapp.com/attachments/608711481969868811/1018414868598112369/7ffbac1b3919b476524f349820e90a39.jpg',
  'https://cdn.discordapp.com/attachments/608711481969868811/1018414868262572072/ac2721a2fddb53766bfd3fa0d363a1cc.jpg',
  'https://cdn.discordapp.com/attachments/608711481969868811/1018414867910230016/a52d5c65ad6640b0cd15e668d0d4af3c.jpg',
  'https://cdn.discordapp.com/attachments/608711481969868811/1018291162374737971/f3b6a974fcd6ea684b7ff85ec69a3707.jpg',
  'https://cdn.discordapp.com/attachments/608711481969868811/1018291162156630036/0771d7b1728c11414e3b940bb7d3d792.jpg',
  'https://cdn.discordapp.com/attachments/608711481969868811/1018291161904984124/af53f31728b2a2647714fac478bf3a70.jpg',
  'https://cdn.discordapp.com/attachments/608711481969868811/1018291161162592286/36f4e7410423a909befba4541acf7f5c.jpg',
  'https://cdn.discordapp.com/attachments/608711481969868811/1018291160881569802/4a7b22f5797eb44ada5dc5141e6622f6.jpg',
  'https://cdn.discordapp.com/attachments/608711481969868811/1018291160151756800/52e07587c6e4d27fe5ababff7bedca54.jpg',
  'https://cdn.discordapp.com/attachments/608711481969868811/1018211053580062820/unknown.png',
  'https://cdn.discordapp.com/attachments/608711481969868811/1018211052867043408/unknown.png',
  'https://cdn.discordapp.com/attachments/608711481969868811/1018211052443406366/unknown.png',
  'https://cdn.discordapp.com/attachments/608711481969868811/1018137854972538991/1662813354402.gif',
  'https://cdn.discordapp.com/attachments/608711481969868811/1018137854569889833/1662813354388.jpg',
  'https://cdn.discordapp.com/attachments/608711481969868811/1018137854272086056/1662813354381.png',
  'https://cdn.discordapp.com/attachments/608711481969868811/1018137854028808212/1662813354372.jpg',
  'https://cdn.discordapp.com/attachments/608711481969868811/1018052114972409957/89b41f16ebf70bf548c8031b476fb191.jpg',
  'https://cdn.discordapp.com/attachments/608711481969868811/1019330043454951554/c441a6db77aa8bb4969285b28e505ee6.jpg',
  'https://cdn.discordapp.com/attachments/608711481969868811/1019330041009684601/0565c8ce1ff527cd13fc377d0a258bbc.jpg',
  'https://cdn.discordapp.com/attachments/608711481969868811/1019739424046727268/d69a75f10c2c99b9be391882eda4b97b.jpg',
  'https://cdn.discordapp.com/attachments/608711481969868811/1019739423820230738/e04e4136c895fb11d9bd06efd2be767d.jpg',
  'https://cdn.discordapp.com/attachments/608711481969868811/1019739423576948867/e2c15399ae880a8150470f80753f86b3.jpg',
  'https://cdn.discordapp.com/attachments/608711481969868811/1019739423346278501/b4848f597885c8d51f0a0477df681844.jpg',
  'https://cdn.discordapp.com/attachments/608711481969868811/1019739423044284546/7f5414eb69d0aa08efdbe6469a3461f2.jpg',
  'https://cdn.discordapp.com/attachments/608711481969868811/1019739422520000573/a709ba6f4b0049f7e1d6f9f9013e8753.jpg',
  'https://cdn.discordapp.com/attachments/608711481969868811/1019676743713435648/SmartSelect_-.png',
  'https://cdn.discordapp.com/attachments/608711481969868811/1019676743449182259/SmartSelect_-_Discord.png',
  'https://cdn.discordapp.com/attachments/608711481969868811/1019676743205933066/SmartSelect_-_Discord.png',
  'https://cdn.discordapp.com/attachments/608711481969868811/1019676742920704020/SmartSelect_-_Discord.png',
  'https://cdn.discordapp.com/attachments/608711481969868811/1019676742622912572/SmartSelect_-_Discord.png',
  'https://cdn.discordapp.com/attachments/608711481969868811/1019676742379655178/SmartSelect_-_Discord.png',
  'https://cdn.discordapp.com/attachments/608711481969868811/1019675515688325191/c3edeaa85140a5ac21469563d0d4afd1.jpg',
  'https://cdn.discordapp.com/attachments/608711481969868811/1019675515487014952/bff7bc9e26fa1122c4234bdbd0499415.jpg',
]
couplesgif = [
  'https://cdn.discordapp.com/attachments/608711480346542102/1017580583469207663/hit_gif_6.gif',
  'https://cdn.discordapp.com/attachments/608711480346542102/1018571269093990410/Couple_PP_Gif_68.gif',
  'https://cdn.discordapp.com/attachments/608711480346542102/1017822994090950706/a_30ff8b1ad24c4d340061293721bd39e7.gif',
  'https://cdn.discordapp.com/attachments/608711480346542102/1017822775446097960/a_6d874dde08bb02e8b14156c0e71595bf.gif',
  'https://cdn.discordapp.com/attachments/608711480346542102/1017822458285396048/7380DF2C-CF6F-476A-A757-434CA48A3868.gif',
  'https://cdn.discordapp.com/attachments/608711480346542102/1019294573970870303/4a2da082cf8d7339c5d28efea3bf0ae0.gif',
  'https://cdn.discordapp.com/attachments/608711480346542102/1019582919003607100/739e167748e257144756217cf930bad1.gif',
  'https://cdn.discordapp.com/attachments/608711480346542102/1019655115457704016/a_30ff8b1ad24c4d340061293721bd39e7.gif'
]
animepng = [
  'https://cdn.discordapp.com/attachments/608711487325995008/1018650218113286195/IMG_1813.jpg',
  'https://cdn.discordapp.com/attachments/608711487325995008/1018289296047870062/ab85225a3657fd369d1dee20d036e019.jpg',
  'https://cdn.discordapp.com/attachments/608711487325995008/1018289294189805648/00dc090b2e90aea174f5fad47d90648f.jpg',
  'https://cdn.discordapp.com/attachments/608711487325995008/1018159501930659860/6b23aaa52d04bc4805ea1eb9b5b5ee9d.jpg',
  'https://cdn.discordapp.com/attachments/608711487325995008/1018159112174960722/IMG-20211219-WA0018.jpg',
  'https://cdn.discordapp.com/attachments/608711487325995008/1018158867374419968/fae0bc26b3c5e337a5152eefe172b04c.jpg',
  'https://cdn.discordapp.com/attachments/608711487325995008/1018158866602676305/IMG_4036.jpg',
  'https://cdn.discordapp.com/attachments/608711487325995008/1018158866019667988/fedf2e14a5e85cc10a31b6115f1f6dec.jpg',
  'https://cdn.discordapp.com/attachments/608711487325995008/1018158865579253861/images_4.jpg',
  'https://cdn.discordapp.com/attachments/608711487325995008/1018158795844755476/ece2f63fe78b11075e1c846efaa1f661.jpg',
  'https://cdn.discordapp.com/attachments/608711487325995008/1018158795572133969/crop.jpg',
  'https://cdn.discordapp.com/attachments/608711487325995008/1018158722490568714/c5ccfb47b7378e295a4d763dca99b844.jpg',
  'https://cdn.discordapp.com/attachments/608711487325995008/1018158721697845399/Avatar_24.png',
  'https://cdn.discordapp.com/attachments/608711487325995008/1018158721442001017/Avatar_26.png',
  'https://cdn.discordapp.com/attachments/608711487325995008/1019328930345394196/Screenshot_20220820_223448.jpg',
  'https://cdn.discordapp.com/attachments/608711487325995008/1019328053618409602/912bb4e363bce997239acb16241a8cbc.jpg',
  'https://cdn.discordapp.com/attachments/608711487325995008/1019326263552385024/1a08260fec87bbf580594edba7ff5f90.jpg',
  'https://cdn.discordapp.com/attachments/608711487325995008/1019612827562029087/3590e741680dfc2430828aa1b3e1b9ad.jpg',
  'https://cdn.discordapp.com/attachments/608711485849337856/1019662778497236992/unknown.png',
]
animegif = [
  'https://cdn.discordapp.com/attachments/608711485849337856/1018263019224051722/a_874eeb773b56296044cbd2ca06312925.gif',
  'https://cdn.discordapp.com/attachments/608711485849337856/1018263021358948417/a_6d0b6cfa566d67b5e386cd9effd9bbf0.gif',
  'https://cdn.discordapp.com/attachments/608711485849337856/1018263027105153054/a_bc8397a09527ebce4029151d0bf212a0.gif',
  'https://cdn.discordapp.com/attachments/608711485849337856/1018263031655972864/a_c87b37c697db3b6ea68021cff251d6f8.gif',
  'https://cdn.discordapp.com/attachments/608711485849337856/1018263041781014599/a_cfb53c1d169b0565e912a4167b78ecf5.gif',
  'https://cdn.discordapp.com/attachments/608711485849337856/1018309682848354404/d4b22bf78ff3c0783b7cd27da14247a7.gif',
  'https://cdn.discordapp.com/attachments/608711485849337856/1018476312245043220/a_50cdf5f3f6bd6470c90edbbc8ff44983.gif',
  'https://cdn.discordapp.com/attachments/608711485849337856/1018855756956717127/1464199626-f0f25477aefb1699b983a5a460c2b12a.gif',
  'https://cdn.discordapp.com/attachments/608711485849337856/1018513399036002314/68809b2508330d3eb74c354fde075270.gif',
  'https://cdn.discordapp.com/attachments/608711485849337856/1018513397131784202/3d6eeea19b1ca264de148652480d8cd6.gif',
  'https://cdn.discordapp.com/attachments/608711485849337856/1018491398158307438/yoriichi.gif',
  'https://cdn.discordapp.com/attachments/608711485849337856/1019369714692149288/0e5465cb74798e4c9105d3b954e6c23f.gif',
  'https://cdn.discordapp.com/attachments/608711485849337856/1019340426563559444/6a2330e2ed77ec9df2075b222e5aa87f.gif',
  'https://cdn.discordapp.com/attachments/608711485849337856/1019268454219534416/unknown.png',
  'https://cdn.discordapp.com/attachments/608711485849337856/1019589246757117982/OldDiratex.gif',
  'https://cdn.discordapp.com/attachments/608711485849337856/1019458139025850478/69d4941f7fcc091c66b596e336e7b39e.gif'
]
banners = [
  'https://cdn.discordapp.com/attachments/857714045251878972/1018592538124353548/cd0a0d4d16c35195cf26ace01a851102.gif',
  'https://cdn.discordapp.com/attachments/857714065710776320/1019245541374308412/images_6.jpg',
  'https://cdn.discordapp.com/attachments/857714065710776320/1018919376424030429/bb0402088285fbf46d0b83c67b258f11.jpg',
  'https://cdn.discordapp.com/attachments/857714065710776320/1018919376143003678/e3d279fe5494844260e4e2fdf072c14d.jpg',
  'https://cdn.discordapp.com/attachments/857714065710776320/1018748387878785094/f853e9172f088d5ffa135ebab82db238.png',
  'https://cdn.discordapp.com/attachments/857714065710776320/1018748387404808222/16453dbb8705d1c8bbf8318f8aa22d73.jpg',
  'https://cdn.discordapp.com/attachments/857714065710776320/1019331744350076928/18b66c364182a6e2f31165658013a483.jpg',
  'https://cdn.discordapp.com/attachments/857714065710776320/1019309957398667325/376415e614690f84e92b6c1709ddfcea.jpg',
  'https://cdn.discordapp.com/attachments/857714065710776320/1019306462478078022/66b1ac8d481fd2f0ca6d8a13cc719dd9.jpg',
  'https://cdn.discordapp.com/attachments/857714065710776320/1019305603392356443/65ab7531f98ab43cfdb69d7a0f0ff7bb.jpg',
  'https://cdn.discordapp.com/attachments/857714065710776320/1019302199584632873/326821a3ff9fe82dc04f7a2fb40ac34f.jpg',
  'https://cdn.discordapp.com/attachments/857714065710776320/1019302188494884924/0bf4e7de34095cc058de8c1557d1d6e2.jpg',
  'https://cdn.discordapp.com/attachments/857714065710776320/1019301900052615268/5753814cceed2b09315b75920df7125f.jpg',
  'https://cdn.discordapp.com/attachments/857714065710776320/1019301880037392494/7ed5f4c66f8e64e55ea5ecba83ec1a25.jpg',
  'https://cdn.discordapp.com/attachments/857714065710776320/1019301874391863316/6ccbfa66ea4a8a186345df6deebd99b5.jpg',
  'https://cdn.discordapp.com/attachments/857714065710776320/1019301868834398319/d0a456f5cb808b972d1bc4369f1e5daa.jpg',
  'https://cdn.discordapp.com/attachments/857714065710776320/1019301864187121714/c4a716a12a0e77da8c6d53b3d6e9f403.jpg',
  'https://cdn.discordapp.com/attachments/857714065710776320/1019301842439643256/b231ee360c213b76286362eb83ff410c.jpg',
  'https://cdn.discordapp.com/attachments/857714045251878972/1019312310474510358/Anka_Code_Girl_Banner_2.gif',
  'https://cdn.discordapp.com/attachments/857714045251878972/1019302079405232218/7c750b26d3d563f1b1affba930c91d4b.gif',
  'https://cdn.discordapp.com/attachments/857714045251878972/1019302076859289659/6cca2105bc742f38dfaa713a3f4276bf.gif',
  'https://cdn.discordapp.com/attachments/857714045251878972/1019302003123441744/950b2c0d071d0ebddac74b1c56cd9913.gif',
  'https://cdn.discordapp.com/attachments/857714045251878972/1019301995418484796/c6242842fe5ee3d67d3b1839dfb0c31e.gif',
  'https://cdn.discordapp.com/attachments/857714045251878972/1019729036190167090/d80eb3916a578456d5d8114a58c84e7b.gif',
  'https://cdn.discordapp.com/attachments/857714045251878972/1019685305990795398/a_efa044c29baf083b2fd19c6c79b36850.gif',
  'https://cdn.discordapp.com/attachments/857714045251878972/1019660928272310283/unknown.png',
  'https://cdn.discordapp.com/attachments/857714045251878972/1019518362285506611/original.gif',
  'https://cdn.discordapp.com/attachments/857714045251878972/1019503558078500874/d7d95c534c9fa8cb16a5b1270cf6ad33.gif',
  'https://cdn.discordapp.com/attachments/768864615676903466/1019727499845959761/a_2386c681f1aea4c4ce5b506c90073613.gif',
  'https://cdn.discordapp.com/attachments/768864495522283560/1019712202418171914/cachedImage.png',
  'https://cdn.discordapp.com/attachments/768864495522283560/1019699791908839445/unknown.png',
  'https://cdn.discordapp.com/attachments/768864495522283560/1019697848842993815/488b7266a37efcc9aebea279f3496dde.png'
]


class pfps(commands.Cog, name="Pfp"):

  def __init__(self, bot):
    self.bot = bot
    self.tasks = []

  def help_custom(self):
    emoji = '<:image:1097042099427360859>'
    label = "Images"
    description = "Shows Images Commands"
    return emoji, label, description

  @commands.hybrid_command()
  async def anime(self, ctx):
    button = discord.ui.Button(label='Gifs', style=discord.ButtonStyle.primary)
    button1 = discord.ui.Button(label='Pic', style=discord.ButtonStyle.success)
    view = discord.ui.View()
    view.add_item(button)
    view.add_item(button1)

    async def button_callback(interaction: discord.Interaction):
      embed5 = discord.Embed(description="Use Buttons For Pfps")
      random_link = random.choice(animegif)
      embed5.set_image(url=random_link)
      await interaction.response.edit_message(embed=embed5)

    async def button1_callback(interaction: discord.Interaction):
      embed6 = discord.Embed(description="Use Buttons For Pfps")
      random_link = random.choice(animepng)
      embed6.set_image(url=random_link)
      await interaction.response.edit_message(embed=embed6)

    embed = discord.Embed(
      description="Use Buttons For Girls Random Pfps / Banners")
    button.callback = button_callback
    button1.callback = button1_callback
    await ctx.reply(embed=embed, view=view)

  @commands.hybrid_command()
  async def couples(self, ctx):
    button = discord.ui.Button(label='Couples Gifs',
                               style=discord.ButtonStyle.primary)
    button1 = discord.ui.Button(label='Couples Pics',
                                style=discord.ButtonStyle.success)
    view = discord.ui.View()
    view.add_item(button)
    view.add_item(button1)

    async def button_callback(interaction: discord.Interaction):
      embed5 = discord.Embed(description="Use Buttons For Pfps")
      random_link = random.choice(couplesgif)
      embed5.set_image(url=random_link)
      await interaction.response.edit_message(embed=embed5)

    async def button1_callback(interaction: discord.Interaction):
      embed6 = discord.Embed(description="Use Buttons For Pfps")
      random_link = random.choice(couplespng)
      embed6.set_image(url=random_link)
      await interaction.response.edit_message(embed=embed6)

    embed = discord.Embed(
      description="Use Buttons For Couples Random Pfps / Banners")
    button.callback = button_callback
    button1.callback = button1_callback
    await ctx.reply(embed=embed, view=view)

  @commands.hybrid_command()
  async def boys(self, ctx):
    button = discord.ui.Button(label='Gifs', style=discord.ButtonStyle.primary)
    button1 = discord.ui.Button(label='Pics',
                                style=discord.ButtonStyle.success)
    view = discord.ui.View()
    view.add_item(button)
    view.add_item(button1)

    async def button_callback(interaction: discord.Interaction):
      embed5 = discord.Embed(description="Use Buttons For Pfps")
      random_link = random.choice(boysgif)
      embed5.set_image(url=random_link)
      await interaction.response.edit_message(embed=embed5)

    async def button1_callback(interaction: discord.Interaction):
      embed6 = discord.Embed(description="Use Buttons For Pfps")
      random_link = random.choice(boyspng)
      embed6.set_image(url=random_link)
      await interaction.response.edit_message(embed=embed6)

    embed = discord.Embed(
      description="Use Buttons For Boys Random Pfps / Banners")
    button.callback = button_callback
    button1.callback = button1_callback
    await ctx.reply(embed=embed, view=view)

  @commands.hybrid_command()
  async def girls(self, ctx):
    button = discord.ui.Button(label='Gifs', style=discord.ButtonStyle.primary)
    button1 = discord.ui.Button(label='Pic', style=discord.ButtonStyle.success)
    view = discord.ui.View()
    view.add_item(button)
    view.add_item(button1)

    async def button_callback(interaction: discord.Interaction):
      embed5 = discord.Embed(description="Use Buttons For Pfps")
      random_link = random.choice(girlsgif)
      embed5.set_image(url=random_link)
      await interaction.response.edit_message(embed=embed5)

    async def button1_callback(interaction: discord.Interaction):
      embed6 = discord.Embed(description="Use Buttons For Pfps")
      random_link = random.choice(girlspng)
      embed6.set_image(url=random_link)
      await interaction.response.edit_message(embed=embed6)

    embed = discord.Embed(
      description="Use Buttons For Girls Random Pfps / Banners")
    button.callback = button_callback
    button1.callback = button1_callback
    await ctx.reply(embed=embed, view=view)

  @commands.hybrid_command()
  async def pic(self, ctx):
    button = discord.ui.Button(label='Pfps', style=discord.ButtonStyle.primary)
    button1 = discord.ui.Button(label='Banners',
                                style=discord.ButtonStyle.success)
    view = discord.ui.View()
    view.add_item(button)
    view.add_item(button1)

    async def button_callback(interaction: discord.Interaction):
      embed5 = discord.Embed(description="Use Buttons For Pfps")
      random_link = random.choice(pfpss)
      embed5.set_image(url=random_link)
      await interaction.response.edit_message(embed=embed5)

    async def button1_callback(interaction: discord.Interaction):
      embed6 = discord.Embed(description="Use Buttons For Pfps")
      random_link = random.choice(banners)
      embed6.set_image(url=random_link)
      await interaction.response.edit_message(embed=embed6)

    embed = discord.Embed(description="Use Buttons For Random Pfps / Banners")
    button.callback = button_callback
    button1.callback = button1_callback
    await ctx.reply(embed=embed, view=view)
