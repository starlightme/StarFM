<template>
  <div class="hello">

    <div class="player">

      <div class="cd">
        <img v-bind:src=mus.songlist[counter].imgurl class="album">
      </div>

      <div class="controller">

        <div class="songinfo">
          <div class="songname">
            <p> {{mus.songlist[counter].name}}</p>
          </div>
        </div>

        <div class="basebar">
          <div class="progressbar" v-bind:style="{ width : progressbar_value + 'px' }"></div>
        </div>


        <div class="buttons">
          <p>test</p>
          <ul>
            <li><i class="fa fa-step-backward fa-lg" aria-hidden="true" @click="lastsong"></i></li>
            <li><i class="fa fa-play fa-lg" aria-hidden="true" @click="playsong"></i></li>
            <li><i class="fa fa-pause fa-lg" aria-hidden="true" @click="pauseplay"></i></li>
            <li><i class="fa fa-step-forward fa-lg" aria-hidden="true" @click="nextsong"></i></li>
          </ul>
          <p>test</p>
        </div>

        <audio v-if="counter < Object.keys(this.mus.songlist).length  "
               v-bind:src=" mus.songlist[counter].url   " id="player" autoplay="autoplay">
          Your browser does not support the audio element.
        </audio>

      </div>

    </div>

    <div class="background"></div>

  </div>

</template>

<script>
  import postData from 'common/music.json'
  export default {
    name: 'hello',
    data () {
      return {
        counter: 0,
        progressbar_value: 0,
        now: 0,
        playtime: 0,
        stop_flag: 0,
        mus: postData,
      }
    },
    watch: {
      counter: function (newClick) {
        console.log(this.counter);

        if (this.counter >= Object.keys(this.mus.songlist).length) {
          this.counter = 0
        }


      },
      now: function (timer) {
        let player = document.getElementById('player');
        this.playtime = this.now / player.duration * 1000
        this.progressbar_value = this.now / player.duration * 230
//        console.log(this.playtime)
        if (this.playtime >= 999) {
          player.pause()
          this.nextsong()
          //清空变量
          this.now = 0
          this.playtime = 0
        }
      }


    },

    mounted () {
//    console.log("开始了")
      //清空变量
      this.now = 0
      this.playtime = 0
      window.setInterval(() => {
        if (this.stop_flag == 0) {
          this.now += 1;
        }

      }, 1000);
    },
    methods: {
      playsong: function () {
        let player = document.getElementById('player');
        player.play();
        this.stop_flag = 0;
      },
      pauseplay: function () {
        let player = document.getElementById('player');
        player.pause();
        this.stop_flag = 1;
      },
      changesong: function () {
        this.now = 0
        this.playtime = 0
        let player = document.getElementById('player');
        player.currentTime = 0;
        player.play();

      },
      nextsong: function () {
        //清空变量
        this.now = 0
        this.playtime = 0
        this.counter += 1
        //清空变量
        this.now = 0
        this.playtime = 0
      },
      lastsong: function () {
        //清空变量
        this.now = 0
        this.playtime = 0
        if (this.counter == 0) {
          this.counter = Object.keys(this.mus.songlist).length - 1
        }
        else {
          this.counter -= 1
        }
        //清空变量
        this.now = 0
        this.playtime = 0
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>



  .cd {
    margin-top: 12%;
    margin-bottom: 1%;
  }

  .album {
    width: 250px;
    margin: 0 106px;
    border-radius: 10%;
    background-repeat: no-repeat;
    background-position: 50% 50%; /* 选取的图像焦点 */
    background-size: cover;
    border: 10px solid hsla(0, 0%, 100%, .5);
    background: white;
    background-clip: padding-box;
  }

  .basebar {

    width: 230px;
    height: 5px;
    margin: 0 120px 0;
    background-color: #414141;
    border-radius: 10px;

  }

  .progressbar {
    width: 0;
    height: 5px;
    color: red;
    text-align: center;
    background-color: #cdd2d7;
    border-radius: 10px;
  }

  .songinfo {
    margin: 0 120px 10px;
    width: 230px;
    height: 15px;
  }

  .songname {
    text-align: center;
    line-height: 15px;
    font-size: 10px;
  }

  .buttons {
    margin: 0 120px 10px;
    width: 230px;
    word-spacing: 30px;
    font-size: 10px;
    border: 5px;
    border-color: transparent;
    border-style: solid;
    text-align: center;

  }

  .buttons i {
    cursor: pointer;
    background: #414141;
    color: #d9d9d9;
    width: 30px;
    height: 30px;
    text-align: center;
    line-height: 30px;
    border-radius: 8px;
    font-size: 10px;
  }

  .buttons p {
    font-size: 5px;
    line-height: 5px;
    visibility: hidden;
  }

  .background {
    position: fixed;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    background: url("../assets/bkimg.jpg") no-repeat center;
    background-size: cover;
    z-index: -1;

  }

  ul li {
    height: 35px;
    line-height: 35px; /*  让内容垂直居中  */
    display: inline; /*  将li设置成内联元素就可以了  */
  }

  .songinfo p {
    /*color: red;*/
    font-family: "Helvetica Neue", Helvetica, Arial, "PingFang SC", "Hiragino Sans GB", "Heiti SC", "Microsoft YaHei", "WenQuanYi Micro Hei", sans-serif;
    font-size: 13px;
    font-weight: 400;
    color: lavender;
  }

</style>
