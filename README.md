# 2019 graduation-design
**注意写一些 tool 的工具方法，成 Util 类**

## 软件结构分析

* 页面部分
* 功能部分
  + 启动页面
  + BasePager和各个子页面
   - BasePager: **公共的pager**
   - VideoPager: **视频播放功能**
   - AudioPager: **音频播放过功能**
  + 切换页面: RadioGroup
  + 屏幕多次初始化数据
  + 顶部标题栏

## 功能点拆分
 1. 启动页面延迟两秒进入主页: 做日期的显示欢迎界面, 类似于豆瓣.
 2. 快速进入主页面，会实例化多个页面: 设置单例模式，从源头控制只能启动一次.
 3. **实现主页面的布局**.
 4. 自定义**RadioButton**.   
 5. 标题栏.
 6. 自定义类继承线性布局，把标题栏布局包在里面.    
 7. 写一个公共的页面 BasePager.
 8. 实现各个页面.
 9. 把页面初始化.
 10. 设置设置**RadioGroup**的监听.
 11. 根据 RadioGroup 的监听切换不同的页面.
 12. **读取本地的视频，在6.0动态获取权限**.
 13. **VideoView ，封装 MediaPlayer 继承 SurfaceView**.
 14. 视频的播放完成的监听，播放出错等监听.
 15. 自定义 VideoView 视频视频全屏和默认值设定.
 16. 手势识别器，双击，单击，长按，n 秒自动隐藏控制面板.
 17. 控制面板绘制.
 18. 屏幕横切换生命周期的屏蔽.
 19. Activity的生命周期.
 20. **EventBus**.
 20. 声音的调节.
 21. 亮度的调节.
 22. 滑动屏幕改变声音和亮度.
 23. 视频进度的更新.
 24. **解码框架简介：ffmpeg ,VLC,Vitmaio**.
 25. **Vitmiao**的集成.
 26. 读取本地音乐.
 27. 播放音乐-Service.
 28. **ServiceConnection**.
 29. 播放器歌曲.
 30. 上一首，下一首.
 31. 设置播放模式.
 32. 通过广播获取当前播放歌曲的事件和名称.
 33. 播放歌曲的进度更新.
 34. 歌词显示控件 ShowLyricView ,继承 TextView.
 35. 绘制歌词.
 36. 解析歌词-一行一行的读取，排序，计算每句高亮显示的时间、歌词同步.
 37. 标题栏.
 38. 软件退出.

 ## time-schedule
### graduation-design(requied)
 task | deadline
 --------------------- | ----------
 Translation doc       | 3.05 ~ 3.10
 Opening report doc    | 3.05 ~ 3.10
 Opening report PPT    | 3.05 ~ 3.10
 Android basical       | 3.10 ~ 3.20
 Media project learning| 3.20 ~ 3.30
 Preliminary completed project| 4.01 ~ 4.10

### person-website(requied)
 task | deadline
 --------------------- | -----------
 Vue learning          | 4.10 ~ 4.20
 ES6                   | 4.20 ~ 4.30
 **CSS 3.0**           | 4.20 ~ 4.30
 webpack               | 4.20 ~ 4.30
 NodeJS                | 4.20 ~ 4.30
 less bootstrap        | 5.01 ~ 5.10
 Vue shop              | 5.01 ~ 5.10
 Vue music             | 5.10 ~ 5.20
 Preliminary completed project| 5.20 ~ 5.30


 ### learning(optional)
  task    |  date
 --------------------- | -----------
  AnglarJS             | 6.01 ~ 6.10
  React                | 6.01 ~ 6.10
  MpVue                | 6.01 ~ 6.10
  Ajax/fetch           | 6.01 ~ 6.10
  Java Spring          | 6.10 ~ 6.20
  docker               | 6.10 ~ 6.20
  linux                | 6.10 ~ 6.20
  shell                | 6.10 ~ 6.20
  DB(mysql 优化/mybatis)| 6.10 ~ 6.20
