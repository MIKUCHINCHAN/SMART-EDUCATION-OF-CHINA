## 背景

被导师安排代看他的网课，受不了傻乎乎地机械刷课，稍微研究了一下发现很简单：该网站看视频时，是间隔50s向服务端发送一个POST请求，服务器再返回相应的进度。



## 用法

登陆后点开一个视频，F12-NETWORK，播放视频一分钟后会出现一个POST请求，该请求内可获得cookie和该视频的orgId、sourceId、segId、itemId、courseId、videoId，再去脚本中修改以上值。



## 注意

①orgId和sourceId是永久不变的，一次获取后一直可用

②segId、itemId、courseId是随着不同课程变化的，同一个课程内所有视频都是相同的

③videoId是每个视频都不一样

④orgId、sourceId、segId、itemId、courseId、videoId还有其他方便的获取方式，自己探索吧！