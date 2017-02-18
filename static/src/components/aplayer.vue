<template>
    <div id="player" class="aplayer"></div>
</template>

<script type="text/javascript">
 import APlayer from 'aplayer'

 export default {
     mounted() {
         var ap = new APlayer({
             element: document.getElementById('player'),
             narrow: false,
             autoplay: false,
             showlrc: 1,
             mutex: true,
             theme: '#444',
             listmaxheight: '128px',
             music:[
                 {
                     title: '的',
                     author: '兔裹煎蛋卷',
                     url: 'http://m2.music.126.net/NOur1yflNcSIovYCQ4uw0Q==/8000046603710904.mp3',
                     pic: 'http://p3.music.126.net/SQF5vSrxTZ5myrmVWxFStQ==/3254554419585268.jpg',
                     lrc: '[by:\u6211\u628a\u5fc3\u4e8b\u5bc4\u6d41\u5e74]\n[00:24.01]\u9f99\u8475\u82b1 \u745f\u7d22\u65e0\u58f0\u65e0\u606f\u7684\u98d8\u843d \r\n[00:29.73]\u4f59\u6e29\u70ed \u88ab\u65e0\u58f0\u7684\u9634\u973e\u96e8\u6df9\u6ca1 \r\n[00:35.61]\u8427\u6740\u6f20 \u9611\u73ca\u9b44 \r\n[00:38.57]\u591a\u5c11\u5e74\u5316\u4e3a\u4e00\u62b9 \r\n[00:41.58]\u591a\u5c11\u4eba \u5728\u8857\u89d2\u64e6\u80a9\u9519\u8fc7 \r\n[00:47.30]\u79bb\u522b\u65f6 \u54ed\u558a\u7740 \r\n[00:50.26]\u4e0d\u820d\u7684\u542b\u60c5\u8109\u8109 \r\n[00:53.13]\u4ed6\u4eec\u8bf4 \u8fd9\u662f\u865a\u4f2a\u7684\u5916\u58f3 \r\n[00:59.00]\u6276\u6851\u6811 \u9c7c\u767d\u9e3d \r\n[01:01.82]\u63a9\u9970\u6697\u6de1\u7684\u5f00\u8131 \r\n[01:04.87]\u4f60\u7ec8\u662f \u662f\u6211\u4e00\u76f4\u6ca1\u6709\u9057\u5fd8\u7684 \r\n[01:12.15]\u94f6\u8033\u956f \u5f00\u4e91\u518c \r\n[01:14.91]\u5915\u9633\u8d64\u7ea2\u7684\u4e00\u62b9 \r\n[01:17.82]\u51b7\u7a97\u5bd2 \u51bb\u4f24\u4e86\u522b\u79bb\u6b32\u8a00\u65f6\u7684\u79bb\u62e9 \r\n[01:23.61]\u67af\u6d69\u679d \u82b1\u6447\u66f3 \r\n[01:26.66]\u54ea\u4e2a\u624d\u662f\u4f60\u771f\u6b63 \r\n[01:29.57]\u7231\u7740\u7684 \r\n[01:31.09]\u6211\u4e0d\u77e5\u6240\u63aa \r\n[01:38.36]\u54ea\u4e00\u4e2a \u54ea\u4e00\u4e2a\u624d\u662f\u4f60\u7231\u7740\u7684 \r\n[01:44.10]\u98ce\u6c99\u8fc7 \u6211\u4eec\u5374\u518d\u4e5f\u672a\u89c1\u5230\u8fc7 \r\n[01:49.97]\u4f60\u8ba9\u6211 \u61c2\u5f97\u4e86 \r\n[01:52.94]\u8fc7\u5ba2\u7ec8\u7a76\u662f\u8fc7\u5ba2 \r\n[01:55.75]\u53ea\u4e3a\u4e86 \u542c\u53e5\u9519\u4e86\u5c31\u8fc7\u4e86 \r\n[02:01.46]\u5fae\u7b11\u7684 \u91ca\u6000\u7684 \r\n[02:04.47]\u542c\u4f60\u8bf4\u5bf9\u4e0d\u8d77\u4e86 \r\n[02:07.38]\u6211\u7ec8\u7a76\u662f\u4f60\u6ca1\u6709\u8bb0\u4f4f\u7684 \r\n[02:13.30]\u653e\u5f03\u4e86 \u5931\u53bb\u4e86 \r\n[02:16.11]\u5c31\u522b\u518d\u60f3\u8fc7\u53bb\u7684 \r\n[02:19.06]\u6d41\u6cea\u4e86 \u4e5f\u8981\u9732\u51fa\u5fae\u7b11\u795d\u798f\u7740 \r\n[02:24.88]\u7eb8\u98de\u673a \u94bb\u77f3\u6212 \r\n[02:27.79]\u8fd8\u6709\u4ec0\u4e48\u820d\u4e0d\u5f97 \r\n[02:30.66]\u662f\u771f\u7684 \u79bb\u5f00\u4e86\u4f60\u6211\u8fd8\u53ef\u4ee5\u5f88\u5feb\u4e50 \r\n[02:36.43]\u8001\u5e08\u8bf4 \u9519\u8bef\u7684 \r\n[02:39.50]\u53ea\u80fd\u7b49\u5f85\u88ab\u6df9\u6ca1 \r\n[02:42.92]\u662f\u7b11\u7684\u8fd8\u662f\u6d41\u6cea\u7684 \r\n[03:11.52]\u90a3\u6761\u8def \u4f60\u7ecf\u8fc7 \r\n[03:14.43]\u8db3\u4ee5\u8ba9\u6211\u7740\u4e86\u9b54 \r\n[03:17.35]\u70df\u706b\u843d \r\n[03:18.85]\u7ec8\u7a76\u5173\u4e8e\u4f60\u7684\u56de\u5fc6\u6709\u592a\u591a \r\n[03:23.21]\u7709\u5934\u9501 \u592a\u6267\u7740 \r\n[03:26.07]\u7ea0\u7f20\u5185\u5fc3\u7684\u6495\u626f \r\n[03:28.98]\u4f60\u8bf4\u7684 \r\n[03:30.34]\u6211\u59cb\u7ec8\u8bb0\u7740 \r\n[03:34.76]\u66fe\u7231\u7684 \u4f24\u6211\u7684 \r\n[03:37.76]\u5446\u5728\u547d\u8fd0\u7684\u957f\u6cb3 \r\n[03:40.73]\u7b49\u7740\u88ab \u51b0\u51b7\u7684\u5fae\u7b11\u7684\u6d41\u6cea\u7684\u6df9\u6ca1 \r\n[03:46.40]\u6709\u4e0d\u820d \u88ab\u770b\u7834 \r\n[03:49.36]\u4f60\u5374\u5047\u88c5\u770b\u4e86\u9519 \r\n[03:52.31]\u60b2\u60c5\u6b4c \r\n[03:53.97]\u70d8\u6258\u7740\u60c5\u6b4c \r\n[03:58.14]\u4fdd\u62a4\u8272 \u53c8\u5982\u4f55 \r\n[04:00.99]\u56de\u60f3\u6709\u4f60\u7684\u65f6\u523b \r\n[04:03.96]\u8fd8\u662f\u4f1a \u81ea\u7136\u800c\u7136\u731d\u5fc3\u7684\u4e0d\u653b\u81ea\u7834 \r\n[04:09.63]\u788e\u7684\u676f \u71c3\u7684\u706b \r\n[04:12.59]\u7684\u5b57\u5728\u89d2\u843d\u9ed8\u9ed8 \r\n[04:15.56]\u7ec8\u7a76\u662f \u6ca1\u6709\u8bb0\u4f4f\u7684 '
                 },
                 {
                     title: '轨迹',
                     author: '徐小薇',
                     url: 'http://m2.music.126.net/1vGFlmmY1NeHEZy_1QuYhA==/5898879883333738.mp3',
                     pic: 'http://p3.music.126.net/EMS4GE-ojql3azwxXYPT3w==/3264450024433079.jpg',
                     lrc: '[00:12.98]\u600e\u4e48\u9690\u85cf\u6211\u7684\u60b2\u4f24\n[00:19.10]\u5931\u53bb\u4f60\u7684\u5730\u65b9\n[00:25.61]\u4f60\u7684\u53d1\u9999\u6563\u7684\u5306\u5fd9\n[00:32.06]\u6211\u5df2\u7ecf\u8ddf\u4e0d\u4e0a\n[00:38.49]\u95ed\u4e0a\u773c\u775b\u8fd8\u80fd\u770b\u89c1\n[00:44.90]\u4f60\u79bb\u53bb\u7684\u75d5\u8ff9\n[00:51.21]\u5728\u6708\u5149\u4e0b\u4e00\u76f4\u627e\u5bfb\u90a3\u60f3\u5ff5\u7684\u8eab\u5f71\n[01:04.48]\u5982\u679c\u8bf4\u5206\u624b\u662f\u82e6\u75db\u7684\u8d77\u70b9\n[01:09.98]\u90a3\u5728\u7ec8\u70b9\u4e4b\u524d\n[01:13.25]\u6211\u613f\u610f\u518d\u7231\u4e00\u904d\n[01:17.25]\u60f3\u8981\u5bf9\u4f60\u8bf4\u7684\n[01:19.89]\u4e0d\u6562\u8bf4\u7684\u7231\n[01:23.52]\u4f1a\u4e0d\u4f1a\u6709\u4eba\u53ef\u4ee5\u660e\u767d\n[01:29.54]\u6211\u4f1a\u53d1\u7740\u5446\u7136\u540e\u5fd8\u8bb0\u4f60\n[01:35.83]\u63a5\u7740\u7d27\u7d27\u95ed\u4e0a\u773c\n[01:42.27]\u60f3\u7740\u90a3\u4e00\u5929\u4f1a\u6709\u4eba\u4ee3\u66ff\n[01:49.10]\u8ba9\u6211\u4e0d\u518d\u60f3\u5ff5\u4f60\n[01:55.10]\u6211\u4f1a\u53d1\u7740\u5446\u7136\u540e\u5fae\u5fae\u7b11\n[02:01.51]\u63a5\u7740\u7d27\u7d27\u95ed\u4e0a\u773c\n[02:07.81]\u53c8\u60f3\u4e86\u4e00\u904d\u4f60\u6e29\u67d4\u7684\u8138\n[02:14.54]\u5728\u6211\u5fd8\u8bb0\u4e4b\u524d\n[02:30.42]\u600e\u4e48\u9690\u85cf\u6211\u7684\u60b2\u4f24\n[02:36.77]\u5931\u53bb\u4f60\u7684\u5730\u65b9\n[02:43.17]\u4f60\u7684\u53d1\u9999\u6563\u7684\u5306\u5fd9\n[02:49.56]\u6211\u5df2\u7ecf\u8ddf\u4e0d\u4e0a\n[02:56.09]\u95ed\u4e0a\u773c\u775b\u8fd8\u80fd\u770b\u89c1\n[03:02.20]\u4f60\u79bb\u53bb\u7684\u75d5\u8ff9\n[03:08.81]\u5728\u6708\u5149\u4e0b\u4e00\u76f4\u627e\u5bfb\u90a3\u60f3\u5ff5\u7684\u8eab\u5f71\n[03:21.81]\u5982\u679c\u8bf4\u5206\u624b\u662f\u82e6\u75db\u7684\u8d77\u70b9\n[03:27.53]\u90a3\u5728\u7ec8\u70b9\u4e4b\u524d\n[03:34.82]\u6211\u613f\u610f\u518d\u7231\u4e00\u904d\n[03:34.68]\u60f3\u8981\u5bf9\u4f60\u8bf4\u7684\n[03:37.69]\u4e0d\u6562\u8bf4\u7684\u7231\n[03:41.11]\u4f1a\u4e0d\u4f1a\u6709\u4eba\u53ef\u4ee5\u660e\u767d\n[03:47.07]\u6211\u4f1a\u53d1\u7740\u5446\u7136\u540e\u5fd8\u8bb0\u4f60\n[03:53.54]\u63a5\u7740\u7d27\u7d27\u95ed\u4e0a\u773c\n[03:59.73]\u60f3\u7740\u90a3\u4e00\u5929\u4f1a\u6709\u4eba\u4ee3\u66ff\n[04:06.86]\u8ba9\u6211\u4e0d\u518d\u60f3\u5ff5\u4f60\n[04:12.96]\u6211\u4f1a\u53d1\u7740\u5446\u7136\u540e\u5fae\u5fae\u7b11\n[04:19.08]\u63a5\u7740\u7d27\u7d27\u95ed\u4e0a\u773c\n[04:25.53]\u53c8\u60f3\u4e86\u4e00\u904d\u4f60\u6e29\u67d4\u7684\u8138\n[04:32.24]\u5728\u6211\u5fd8\u8bb0\u4e4b\u524d\n\n[04:38.34]\u6211\u4f1a\u53d1\u7740\u5446\u7136\u540e\u5fd8\u8bb0\u4f60\n[04:45.05]\u63a5\u7740\u7d27\u7d27\u95ed\u4e0a\u773c\n[04:51.10]\u60f3\u7740\u90a3\u4e00\u5929\u4f1a\u6709\u4eba\u4ee3\u66ff\n[04:58.01]\u8ba9\u6211\u4e0d\u518d\u60f3\u5ff5\u4f60\n[05:03.89]\u6211\u4f1a\u53d1\u7740\u5446\u7136\u540e\u5fae\u5fae\u7b11\n[05:10.25]\u63a5\u7740\u7d27\u7d27\u95ed\u4e0a\u773c\n[05:16.70]\u53c8\u60f3\u4e86\u4e00\u904d\u4f60\u6e29\u67d4\u7684\u8138\n[05:23.50]\u5728\u6211\u5fd8\u8bb0\u4e4b\u524d\n\n[05:29.62]\u5fc3\u91cc\u7684\u773c\u6cea\n[05:32.81]\u6a21\u7cca\u4e86\u89c6\u7ebf\n[05:36.57]\u4f60\u5df2\u5feb\u770b\u4e0d\u89c1'
                 },
                 {
                     title: '长安忆',
                     author: '双笙',
                     url: 'http://m2.music.126.net/01nB_xGVjohvr5rNi0T62Q==/18719185463617559.mp3',
                     pic: 'http://p4.music.126.net/e1HH9QrWkm363ham5-3vwA==/18159534044891468.jpg',
                     lrc: '[by:\u672c\u7ef4\u7b11]\n[00:22.30]\u957f\u5b89\u96e8\r\n[00:24.43]\u4e00\u591c\u843d\u79cb\u610f \r\n[00:27.87]\u8def\u5343\u91cc\r\n[00:29.88]\u6714\u98ce\u5439\u5ba2\u8863 \r\n[00:33.47]\u6c5f\u8239\u591c\u96e8\u542c\u7b1b\r\n[00:36.73]\u501a\u665a\u6674 \r\n[00:39.40]\u5e73\u6c99\u6f20\u6f20\u516e\u6101\u65e0\u9645 \r\n[00:45.60]\u957f\u5b89\u5824\r\n[00:46.93]\u5782\u6768\u9001\u522b\u79bb \r\n[00:50.49]\u5343\u5c71\u6708\r\n[00:52.60]\u4e00\u7247\u4f24\u5fc3\u78a7 \r\n[00:56.80]\u957f\u95e8\u53c8\u8bef\u4f73\u671f\r\n[00:59.59]\u58f0\u6e05\u51c4 \r\n[01:02.80]\u6731\u989c\u67d3\u5c18\u516e\u68a6\u4e2d\u8bed \r\n[01:10.20]\u4e8c\u5341\u4e09\u5f26\u6025\r\n[01:13.24]\u843d\u82b1\u4eba\u72ec\u7acb \r\n[01:15.74]\u60df\u6709\u6b64\u66f2\u80fd\u5bc4\u5fc3\u4e2d\u610f \r\n[01:21.49]\u6708\u843d\u5b50\u89c4\u557c\r\n[01:24.53]\u98de\u7d6e\u8854\u971c\u53bb \r\n[01:27.23]\u7136\u8bfa\u91cd\r\n[01:28.90]\u53ea\u613f\u541b\u4ece\u6b64\u8bb0 \r\n[01:44.20]\u957f\u5b89\u53bb\r\n[01:45.96]\u8f9e\u5bb6\u4e09\u5343\u91cc \r\n[01:49.73]\u6daf\u65e0\u57a0\r\n[01:51.80]\u5374\u95ee\u6101\u51e0\u8bb8 \r\n[01:55.10]\u8bd5\u5251\u66f4\u987b\u949f\u5415\uff0c\u4f34\u541b\u8d77 \r\n[02:01.20]\u98ce\u6e21\u8427\u8427\u516e\u70df\u8ff7\u79bb \r\n[02:06.64]\u957f\u5b89\u5c45\r\n[02:08.50]\u9647\u5934\u8c01\u5439\u7b1b \r\n[02:12.31]\u706f\u82b1\u843d\r\n[02:14.38]\u7626\u5c3d\u53c8\u4e00\u5915 \r\n[02:17.84]\u9189\u4e61\u8def\u9690\u96be\u884c\r\n[02:21.12]\u98ce\u9732\u6e05 \r\n[02:23.75]\u541b\u5411\u6f47\u6e58\u516e\u6211\u5411\u79e6 \r\n[02:31.88]\u9189\u7b11\u4e09\u5343\u5e2d\r\n[02:35.15]\u4e0d\u8bc9\u79bb\u522b\u610f\r\n[02:37.56]\u60df\u6709\u6b64\u66f2\u80fd\u5fd8\u4eba\u95f4\u666f \r\n[02:43.31]\u5e74\u534e\u843d\u4e39\u9752\r\n[02:46.53]\u4e00\u7247\u78a7\u7a7a\u6d17\r\n[02:48.91]\u77e5\u97f3\u7a00\r\n[02:50.80]\u5f26\u65ad\u6709\u8c01\u6765\u542c \r\n[03:20.56]\u843d\u65e5\u5b64\u57ce\u95ed\r\n[03:23.35]\u71d5\u7136\u5f52\u65e0\u8ba1 \r\n[03:25.59]\u60df\u6709\u6b64\u66f2\u80fd\u89e3\u65ad\u80a0\u60c5 \r\n[03:31.29]\u8fb9\u58f0\u8fde\u89d2\u8d77\r\n[03:34.40]\u4eba\u53bb\u65e0\u7559\u610f \r\n[03:36.96]\u7f8c\u7ba1\u96be\u7eed\r\n[03:40.57]\u60a0\u60a0\u971c\u6ee1\u5730 \r\n[03:42.86]\u53bb\u7559\u4e24\u65e0\u610f\r\n[03:45.91]\u505c\u4e91\u676f\u96be\u606f \r\n[03:48.27]\u6b64\u66f2\u58f0\u6210\r\n[03:50.46]\u81ea\u6709\u8eab\u540e\u540d \r\n[03:53.93]\u957f\u5b89\u5fc6\r\n[03:55.82]\u91cd\u697c\u501a\u57ce\u9685 \r\n[03:59.25]\u964c\u4e0a\u96ea\r\n[04:01.52]\u6c89\u9189\u590d\u53c8\u9192 \r\n[04:05.80]\u65e9\u77e5\u5982\u6b64\u76f8\u9047\r\n[04:08.31]\u4e0d\u5982\u4e0d\u9047 \r\n[04:11.70]\u7b19\u6b4c\u6b47\u5c3d\u516e\u4eba\u6563\u53bb\u0000',
                 }
             ]

         });
         ap.init;
     }

 }
</script>

<style>
 .aplayer {
     text-align:center;
     margin:auto;
     /* max-width:480px; */
     background-color:rgba(255, 255, 255, 0.5);
 }
 .aplayer .aplayer-lrc {
     display: none;
     position: relative;
     height: 30px;
     background: rgba(255, 255, 255, 0);
     text-align: center;
     overflow: hidden;
     margin: -10px 0 7px;
 }
 .aplayer .aplayer-lrc:before {
     height: 0%;
 }
 .aplayer .aplayer-lrc:after {
     height: 0%;
 }
 .aplayer .aplayer-info .aplayer-controller .aplayer-time {
     color: #444;
 }
 .aplayer .aplayer-lrc p {
     color: #a40000;
 }
 .aplayer .aplayer-list ol li.aplayer-list-light {
     background: rgba(255, 255, 255, 0.4);
 }
 .aplayer .aplayer-list ol li:hover {
     background: rgba(255, 255, 255, 0.5);
 }
</style>
