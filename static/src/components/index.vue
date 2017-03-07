<template>
  <div>
    <div data-example-id="carousel-with-captions">
      <div id="carousel-example-captions" class="carousel slide" data-ride="carousel">
        <ol class="carousel-indicators">
          <li data-target="#carousel-example-captions" data-slide-to="0" class="active"></li>
          <li data-target="#carousel-example-captions" data-slide-to="1" class=""></li>
          <li data-target="#carousel-example-captions" data-slide-to="2" class=""></li>
        </ol>
        <div class="carousel-inner" role="listbox">
          <div class="item active">
            <img src="/static/images/bg1.jpg" style="height:300px;width:100%">
            <div class="carousel-caption">
              <h3>First slide label</h3>
              <p>Nulla vitae elit libero, a pharetra augue mollis interdum.</p>
            </div>
          </div>
          <div class="item" v-for="carousel in carousels">
            <img :src="carousel.url" alt="..." style="height:300px;width:100%">
            <div class="carousel-caption">
              <h3>{{ carousel.title }}</h3>
              <p>{{ carousel.description }}</p>
            </div>
          </div>
        </div>
        <a class="left carousel-control" href="#carousel-example-captions" role="button" data-slide="prev">
          <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
          <span class="sr-only">Previous</span>
        </a>
        <a class="right carousel-control" href="#carousel-example-captions" role="button" data-slide="next">
          <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
          <span class="sr-only">Next</span>
        </a>
      </div>
    </div>
    <br/>
    <div class="row">
      <div class="page-header text-center" style="margin-top:10px;margin-bottom:10px;">
        <h3>Example page header</h3>
      </div>
      <div class="col-sm-6 col-md-3" v-for="picture in pictures">
        <div class="thumbnail" style="padding:0;border-radius:5px;">
          <img :src="picture.url" alt="">
          <div class="caption">
            <h3>{{ picture.title }}</h3>
            <p>{{ picture.description }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
 export default {
     data () {
         return {
             pictures:[
                 {"title":"11","description":"222","url":"./static/images/bg1.jpg"},
                 {"title":"11",
                  "description":"Cras justo odio, dapibus ac facilisis in, egestas eget quam. Donec id elit non mi porta gravida at eget metus. Nullam id dolor id nibh ultricies vehicula ut id elit.",
                  "url":"./static/images/bg1.jpg"},
                 {"title":"11","description":"222","url":"./static/images/bg1.jpg"},
                 {"title":"11","description":"222","url":"./static/images/bg1.jpg"},
             ],
             carousels:[
                 {"title":"11","description":"222","url":"./static/images/bg1.jpg"},
                 {"title":"11","description":"222","url":"./static/images/bg1.jpg"}
             ]
         }
     }
 }
</script>
