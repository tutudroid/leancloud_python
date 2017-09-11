<template>
 <div class="editMarketCategory">
  <h2 @click="addFirstHtml()" class="addBtn"><span class="glyphicon glyphicon-plus"></span>加一级分类</h2>
  <div class="cateContent">
    <h3 class="save link" @click="save()">保存</h3>
    <h3 class="oprate"><span class="title">分类名称</span><span class="title">添加图片</span><span class="title">分类简介</span><span class="title">操作</span></h3>
    <div class="marketCate" v-if="marketcategorys.length>0">

      <div class='grandFather mainContent' v-for='fcategory in marketcategorys'>
        <span id="f" class='glyphicon glyphicon-triangle-bottom' @click="hide($event)"></span>
        <input type='text' class='grandFatherInput' :value='fcategory.name' :id="fcategory.objectId" :uniqueId="fcategory.uniqueId">
        <label :for="'file'+fcategory.objectId" @click="changeImage($event)">添加或改变图片</label>
        <input class="file" :id="'file'+fcategory.objectId" type="file">
        <div :id="'prev_file'+fcategory.objectId" class="prev_container">
          <div class="prev_thumb" :style="'background-image:url('+fcategory.mainImage+')'"></div>
        </div>
        <textarea rows="7" cols="20" class="grandFatherDescription">{{fcategory.briefDescription}}</textarea>
        <span class='glyphicon glyphicon-remove remove link' @click="deleteFirst($event)"></span>
        <hr>
        <div class='father' v-for='scategory in fcategory.saleCategorySecond' v-if='scategory!=null'>
          <span class='directLine'></span>
          <span id="f" class='glyphicon glyphicon-triangle-bottom' @click="hide($event)"></span>
          <input type='text' class='fatherInput' :value="scategory.name" :id="scategory.objectId" :uniqueId="scategory.uniqueId">
          <label v-bind:for="'file'+scategory.objectId" @click="changeImage($event)">添加或改变图片</label>
          <input class="file" :id="'file'+scategory.objectId" type="file">
          <div :id="'prev_file'+scategory.objectId" class="prev_container">
            <div class="prev_thumb" :style="'background-image:url('+scategory.mainImage+')'"></div>
          </div>
          <textarea rows="7" cols="20" class="fatherDescription" ></textarea>
          <span class='glyphicon glyphicon-remove remove link' @click="deleteSecond($event)"></span>
          <hr>
        </div>
        <div class='addSecond'>
          <span class='directLine'></span>
          <span class='btn btn-primary secondAdd' @click="addSecondHtml">添加二级子分类</span>
          <hr  class='lastHr' style='border-top:3px solid #a00404'>
        </div>
      </div>

    </div>
  </div>
 </div>
</template>

<script>
  $(document).ready(function()
  {
    
  });
  export default{
  
    data:function(){
     return{
      count:0,
      firstCount:0,
      secondCount:0,
      thirdCount:0,
      first:[],
      second:[],
      third:[],
      index:[],
      fcount:0,
      scount:80,
     }
    },
    props:['marketcategorys'],
    methods:{
      changeImage(e){
        let id = 'input#' + $(e.target).attr('for');
        $(id).preimage();
      },
      addFirstHtml(){
        let _this = this; 
        let firstHtml = "<div class='grandFather mainContent'><span id='f"+this.fcount+"' class='glyphicon glyphicon-triangle-bottom'></span><input type='text' class='grandFatherInput'><label for='file"+this.fcount+"'>添加或改变图片</label><input class='file' id='file"+this.fcount+"' type='file' hidden><div id='prev_file"+this.fcount+"' class='prev_container'></div><textarea rows='7' cols='20' class='grandFatherDescription'></textarea><span class='glyphicon glyphicon-remove remove link'></span><hr><div class='father'><span class='directLine'></span><span id='s"+this.scount+"' class='glyphicon glyphicon-triangle-bottom'></span><input type='text' class='fatherInput'><label for='file"+this.scount+"'>添加或改变图片</label><input class='file' id='file"+this.scount+"' type='file' hidden><div id='prev_file"+this.scount+"' class='prev_container'></div><textarea rows='7' cols='20' class='fatherDescription'></textarea><span class='glyphicon glyphicon-remove remove link'></span><hr></div><div class='addSecond'><span class='directLine'></span><span id='adds"+this.fcount+"' class='btn btn-primary secondAdd'>添加二级子分类</span></div><hr class='lastHr' style='border-top:3px solid #a00404'></div>";
      	$(firstHtml).prependTo('.marketCate');
        let secondAdd = '#adds'+this.fcount;
      	$(secondAdd).bind('click',function(event){
      	  _this.addSecondHtml(event);
      	});
        $('.grandFather .remove').bind('click',function(event){
          _this.deleteFirst(event);
        });
        $('.father .remove').bind('click',function(event){
          _this.deleteSecond(event);
        });
        let ftriangle = '#f'+this.fcount;
        $(ftriangle).bind('click',function(event){
          _this.hide(event);
        });
        let striangle = '#s'+this.scount;
        $(striangle).bind('click',function(event){
          _this.hide(event);
        });
        let file1 = '#file'+this.fcount;
        let file2 = '#file'+this.scount;
        $(document).ready(function()
        {
          $(file1).preimage();
        });
        $(document).ready(function()
        {
          $(file2).preimage();
        });
        this.fcount++;
        this.scount++;
      },
      addSecondHtml(event){
        let _this = this;
        let targetSecond = $(event.currentTarget).parent().parent();
      	let button = $(event.currentTarget).parent();
      	let secondHtml = '<div class="father"><span class="directLine"></span><span id="s'+this.scount+'" class="glyphicon glyphicon-triangle-bottom"></span><input type="text" class="fatherInput"><label for="file'+this.scount+'">添加或改变图片</label><input class="file" id="file'+this.scount+'" type="file" hidden><div id="prev_file'+this.scount+'" class="prev_container"></div><textarea rows="7" cols="20" class="fatherDescription"></textarea><span class="glyphicon glyphicon-remove remove link"></span><hr></div>';
      	$(secondHtml).insertBefore(targetSecond.children('.lastHr'));
      	$(button).insertBefore(targetSecond.children('.lastHr'));
        $('.father .remove').bind('click',function(event){
          _this.deleteSecond(event);
        });
        let striangle = '#s'+this.scount;
        $(striangle).bind('click',function(event){
          _this.hide(event);
        });
        this.scount++;
      },
      deleteFirst(e){
        let objectId = $(e.currentTarget).prev().attr('id');
        let grandFatherInput = $(e.currentTarget).prev();
        let grandFatherDiv = $(e.currentTarget).parent();
        if(grandFatherDiv.children('.father').length>0){
          swal("无法删除","第一级下面有子级的存在");
        }else{
          swal({
            title: "你确定吗?",
            text: "删除之后将无法恢复",
            type: "warning",
            showCancelButton: true,
            confirmButtonColor: "#DD6B55",
            confirmButtonText: "是的,我要删除它!",
            closeOnConfirm: false
          },
          function(){
            $.ajax({
                type: 'get',
                url: '/Product/DelSaleCategory/',
                data: {
                   StoreCategory: 'SaleCategoryFirst',
                   objectId: objectId,
                },
                success: function (data) {
                  swal("成功删除");
                  grandFatherDiv.remove();               
                },
               error: function(XMLHttpRequest, textStatus, errorThrown) {
                 swal("无法删除");
                },
            });
          });
        }
      },
      deleteSecond(e){
        let objectId = $(e.currentTarget).prev().attr('id');
        let fatherInput = $(e.currentTarget).prev();
        let fatherDiv = $(e.currentTarget).parent();
        if(fatherDiv.children('.son').length>0){
          swal("无法删除","第二级下面有子集的存在");
        }else{
          swal({
            title: "你确定吗?",
            text: "删除之后将无法恢复",
            type: "warning",
            showCancelButton: true,
            confirmButtonColor: "#DD6B55",
            confirmButtonText: "是的,我要删除它!",
            closeOnConfirm: false
          },
          function(){
            $.ajax({
                type: 'get',
                url: '/Product/DelSaleCategory/',
                data: {
                   StoreCategory: 'SaleCategorySecond',
                   objectId: objectId,
                },
                success: function (data) {
                  swal("成功删除");
                  fatherDiv.remove();               
                },
               error: function(XMLHttpRequest, textStatus, errorThrown) {
                 swal("无法删除");
                },
            });
          });
        }
      },
      hide(e){
        let div = $(e.currentTarget).parent();
        let fhideTarget = $(div).children('.father');
        let fhideAdd = $(div).children('.addSecond');
        if(fhideTarget.length > 0){
          for(let prop in fhideTarget){
            if(prop > -1){
              $(fhideTarget[prop]).toggleClass( 'hideCategory', 'hideCategory' );
            }else{
              break;
            }
          }
          fhideAdd.toggleClass( 'hideCategory', 'hideCategory' );
          $(div).children('span[id*="f"]').toggleClass('glyphicon-triangle-bottom','glyphicon-triangle-bottom');
          $(div).children('span[id*="f"]').toggleClass('glyphicon-triangle-right','glyphicon-triangle-right');
        }
      },
      save(){
        let foo = $('.grandFather');
        let grandFatherDiv = [];
        let hasEmpty = false;
        for(let prop in foo){
          if(prop > -1){
            grandFatherDiv.push(foo[prop]);
          }
        }
        let grandFatherInputObject = grandFatherDiv.map(function(obj){
            let grandFatherInputObject = {};
            let fInput = $(obj).children('.grandFatherInput').val();
            grandFatherInputObject.objectId = $(obj).children('.grandFatherInput').attr('id');
            grandFatherInputObject.name = fInput;
            grandFatherInputObject.uniqueId = $(obj).children('.grandFatherInput').attr('uniqueId');
            let fDescription = $(obj).children('textarea').val();
            grandFatherInputObject.briefDescription = fDescription;
            if($('.grandFather').children('div[id*="prev_file"]').children('.prev_thumb').length > 0){
              let fImage = $('.grandFather').children('div[id*="prev_file"]').children('.prev_thumb').attr('style').slice(23);
              grandFatherInputObject.mainImage = fImage;
            }else{
              grandFatherInputObject.mainImage = "";
              hasEmpty = true;
            }
            grandFatherInputObject.saleCategorySecond = [];
            let foo = $(obj).children('.father');
            let fatherDiv = [];
            for(let prop in foo){
                if(prop > -1){
                    fatherDiv.push(foo[prop]);
                }else{
                    break;
                }
            }
            let fatherInputObject = fatherDiv.map(function(obj){
                let fatherInputObject = {};
                let sInput = $(obj).children('.fatherInput').val();
                fatherInputObject.objectId = $(obj).children('.fatherInput').attr('id');
                fatherInputObject.name = sInput;    
                fatherInputObject.uniqueId = $(obj).children('.fatherInput').attr('uniqueId');  
                let sDescription = $(obj).children('textarea').val();
                fatherInputObject.briefDescription = sDescription;  
                if($('.grandFather').children('div[id*="prev_file"]').children('.prev_thumb').length > 0){
                  let sImage = $('.father').children('div[id*="prev_file"]').children('.prev_thumb').attr('style').slice(23);
                  fatherInputObject.mainImage = sImage;
                }else{
                  fatherInputObject.mainImage = "";
                  hasEmpty = true;
                }               
                return fatherInputObject;
            });
            grandFatherInputObject.saleCategorySecond = fatherInputObject;
            return grandFatherInputObject;
        }); 
        if(hasEmpty){
          swal("你有图片没有上传");
        }else{
          let obj = {};
          obj.StoreCategoryFirst = [];
          obj.StoreCategoryFirst = grandFatherInputObject;
          swal({
            title: "你确定更新销售分类吗?",
            text: "更新之后将无法恢复",
            type: "warning",
            showCancelButton: true,
            confirmButtonColor: "#DD6B55",
            confirmButtonText: "是的,我要更新它!",
            closeOnConfirm: false
          },
          function(){
            $.ajax({
              type: 'POST',
              url: '/Product/ShowSaleCategory/',
              headers: {
                'X-CSRFToken': $('input[name="csrfmiddlewaretoken"]').prop('value')
              },
              contentType: "application/json; charset=utf-8",
              dataType: "json",
              data: JSON.stringify(obj),
              success: function (data) {
                swal("销售分类已经更新为最新版");
              },
              error: function(XMLHttpRequest, textStatus, errorThrown) {
                swal("销售分类更新失败");
              },           
            });
          });
        }
      },
    },
  }
</script>

<style lang="scss">
  .editMarketCategory{
    .addBtn{
      border-radius: 10px;
      width: 170px;
      background-color: antiquewhite;
      margin-top: 20px;
      border: 2px solid;
      font-size: 20px;
      cursor:pointer;
    }
    .title{
      margin-right: 280px;
      font-size: large;
    }
    .oprate{
      background-color: burlywood;
    }
    .fatherInput{
      position: relative;
      left: 50px;
      bottom:90px;
    }
    .grandFatherInput{
      position: relative;
      left: 50px;
      bottom:90px;
    }
    .secondAdd{
      position: relative;
      left:50px;
      bottom:90px;
    }
    .directLine{
      width: 50px;
      height: 50px;
      display: inline-block;
      border-bottom: 2px solid;
      border-left: 2px solid;
      position: relative;
      left: 45px;
      bottom: 98px;
    }
    .grandFather label{
      height: 100px;
      background-color: #c7c7ae;
      display: inline-block;
      position: relative;
      left: 80px;
      cursor: pointer;
      bottom: 120px;
      box-shadow: 1px 2px sandybrown;
      color: black;
      text-shadow: 1px 2px seashell;
    }
    .father label{
      height: 100px;
      background-color: #c7c7ae;
      display: inline-block;
      position: relative;
      left: 80px;
      cursor: pointer;
      box-shadow: 1px 2px sandybrown;
      color: black;
      text-shadow: 1px 2px seashell;
    }
    .grandFather .grandFatherDescription{
        height: 150px;
        position: relative;
        left: 280px;
    }
    .father .fatherDescription{
        height: 150px;
        position: relative;
        left: 250px;
    }
    .father .glyphicon-triangle-bottom,.father .glyphicon-triangle-right{
      position:relative;
      left: 45px;
      top:-90px;
      left:47px;
    }
    .grandFather .glyphicon-triangle-bottom,.grandFather .glyphicon-triangle-right{
      position:relative;
      top:-90px;
      left: 47px;
    }
    .directLine.add{
      left: 55px;
      bottom:90px;
    }

    .remove{
      position: relative;
      left: 510px;
      top:-90px;
    }
    .father .remove{
      left: 460px;
    }
    .mainContent{
      position: relative;
      left: 40px;
      top: 10px;
    }
    .hideCategory{
      display:none;
    }
    .showCategory{
      display:initial;
    }
    input[type=file]{
      display: none;
    }
    div[id*=prev_file]{
      display:inline;
    }
    .prev_container{
      overflow: auto;
      width: 300px;
      height: 135px;
    }

    .prev_thumb{
      margin: 10px;
      height: 100px;
      width: 100px;
    }
    .prev_container{
      float:right;
    }

  }
</style>

