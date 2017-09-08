<template>
 <div class="editStockCategory">
  <h2 @click="addFirstHtml()" class="addBtn"><span class="glyphicon glyphicon-plus"></span>加一级分类</h2>
  <div class="cateContent">
    <h3 class="save link" @click="save()">保存</h3>
    <h3 class="oprate"><span class="title">分类名称</span><span class="title">--</span><span class="title">操作</span></h3>
    <div class="stockCate">
      <div class='grandFather mainContent' v-for='fcategory in stockcategorys'><span id="f" class='glyphicon glyphicon-triangle-bottom' @click="hide($event)"></span><input type='text' class='grandFatherInput' :value='fcategory.name' :id="fcategory.objectId"><span class='glyphicon glyphicon-remove remove link' @click="deleteFirst($event)"></span><hr><div class='father' v-for='scategory in fcategory.storeCategorySecond'><span class='directLine'></span><span id="f" class='glyphicon glyphicon-triangle-bottom' @click="hide($event)"></span><input type='text' class='fatherInput' :value="scategory.name" :id="scategory.objectId"><span class='glyphicon glyphicon-remove remove link' @click="deleteSecond($event)"></span><hr><div class='son' v-for='tcategory in scategory.storeCategoryThird'><span class='directLine add'></span><span class='glyphicon glyphicon-triangle-bottom'></span><input type='text' class='sonInput' :value='tcategory.name' :id="tcategory.objectId"><span class='glyphicon glyphicon-remove remove link' @click="deleteThird($event)"></span><hr></div><div class='addThird'><span class='directLine add'></span><span class='btn btn-primary thirdAdd' @click="addThirdHtml($event)">添加三级子分类</span><hr></div></div><div class='addSecond'><span class='directLine'></span><span class='btn btn-primary secondAdd' @click="addSecondHtml">加二级子分类</span></div><hr  class='lastHr' style='border-top:3px solid #a00404'></div>
    </div>
  </div>
 </div>
</template>

<script>
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
      scount:0,
     }
    },
    props:['stockcategorys'],
    methods:{
      addFirstHtml(){
        let _this = this; 
        let firstHtml = "<div class='grandFather mainContent'><span id='f"+this.fcount+"' class='glyphicon glyphicon-triangle-bottom'></span><input type='text' class='grandFatherInput'><span class='glyphicon glyphicon-remove remove link'></span><hr><div class='father'><span class='directLine'></span><span id='s"+this.scount+"' class='glyphicon glyphicon-triangle-bottom'></span><input type='text' class='fatherInput'><span class='glyphicon glyphicon-remove remove link'></span><hr><div class='son'><span class='directLine add'></span><span class='glyphicon glyphicon-triangle-bottom'></span><input type='text' class='sonInput'><span class='glyphicon glyphicon-remove remove link'></span><hr></div><div class='addThird'><span class='directLine add'></span><span id='addt"+this.scount+"' class='btn btn-primary thirdAdd'>添加三级子分类</span><hr></div></div><div class='addSecond'><span class='directLine'></span><span id='adds"+this.fcount+"' class='btn btn-primary secondAdd'>添加二级子分类</span></div><hr class='lastHr' style='border-top:3px solid #a00404'></div>";
      	$(firstHtml).prependTo('.stockCate');
        let secondAdd = '#adds'+this.fcount;
      	$(secondAdd).bind('click',function(event){
      	  _this.addSecondHtml(event);
      	});
        let thirdAdd = '#addt'+this.scount;
      	$(thirdAdd).bind('click',function(event){
      	  _this.addThirdHtml(event);
      	});
        $('.grandFather .remove').bind('click',function(event){
          _this.deleteFirst(event);
        });
        $('.father .remove').bind('click',function(event){
          _this.deleteSecond(event);
        });
        $('.son .remove').bind('click',function(event){
          _this.deleteThird(event);
        });
        let ftriangle = '#f'+this.fcount;
        $(ftriangle).bind('click',function(event){
          _this.hide(event);
        });
        let striangle = '#s'+this.scount;
        $(striangle).bind('click',function(event){
          _this.hide(event);
        });
        this.fcount++;
        this.scount++;
      },
      addSecondHtml(event){
        let _this = this;
        let targetSecond = $(event.currentTarget).parent().parent();
      	let button = $(event.currentTarget).parent();
      	let secondHtml = '<div class="father"><span class="directLine"></span><span id="s'+this.scount+'" class="glyphicon glyphicon-triangle-bottom"></span><input type="text" class="fatherInput"><span class="glyphicon glyphicon-remove remove link"></span><hr><div class="son"><span class="directLine add"></span><span class="glyphicon glyphicon-triangle-bottom"></span><input type="text" class="sonInput"><span class="glyphicon glyphicon-remove remove link"></span><hr></div><div class="addThird"><span class="directLine add"></span><span id="addt'+this.scount+'" class="btn btn-primary thirdAdd">添加三级子分类</span><hr></div></div>';
      	$(secondHtml).insertBefore(targetSecond.children('.lastHr'));
      	$(button).insertBefore(targetSecond.children('.lastHr'));
        let thirdAdd = '#addt'+this.scount;
        $(thirdAdd).bind('click',function(event){
          _this.addThirdHtml(event);
        });
        $('.father .remove').bind('click',function(event){
          _this.deleteSecond(event);
        });
        $('.son .remove').bind('click',function(event){
          _this.deleteThird(event);
        });
        let striangle = '#s'+this.scount;
        $(striangle).bind('click',function(event){
          _this.hide(event);
        });
        this.scount++;
      },
      addThirdHtml(event){
        let _this = this;
        let targetThird = $(event.currentTarget).parent().parent();
        let button = $(event.currentTarget).parent();
      	let thirdHtml = '<div class="son"><span class="directLine add"></span><span class="glyphicon glyphicon-triangle-bottom"></span><input type="text" class="sonInput"><span class="glyphicon glyphicon-remove remove link"></span><hr></div>';
      	$(thirdHtml).appendTo(targetThird);
        $(button).appendTo(targetThird);
        $('.son .remove').bind('click',function(event){
          _this.deleteThird(event);
        });
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
                url: '/Product/DelStoreCategory/',
                data: {
                   StoreCategory: 'StoreCategoryFirst',
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
                url: '/Product/DelStoreCategory/',
                data: {
                   StoreCategory: 'StoreCategorySecond',
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
      deleteThird(e){
        let objectId = $(e.currentTarget).prev().attr('id');
        let sonInput = $(e.currentTarget).prev();
        let sonDiv = $(e.currentTarget).parent();
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
              url: '/Product/DelStoreCategory/',
              data: {
                 StoreCategory: 'StoreCategoryThird',
                 objectId: objectId,
              },
              success: function (data) {
                swal("成功删除");
                sonDiv.remove();               
              },
             error: function(XMLHttpRequest, textStatus, errorThrown) {
               swal("无法删除");
              },
          });
        });
      },
      hide(e){
        let div = $(e.currentTarget).parent();
        let fhideTarget = $(div).children('.father');
        let fhideAdd = $(div).children('.addSecond');
        let shideTarget = $(div).children('.son');
        let thideAdd = $(div).children('.addThird');
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
        if(shideTarget.length > 0){
          for(let prop in shideTarget){
            if(prop > -1){             
              $(shideTarget[prop]).toggleClass( 'hideCategory', 'hideCategory' ); 
            }else{
              break;
            }
          }
          thideAdd.toggleClass( 'hideCategory', 'hideCategory' );
          $(div).children('span[id*="s"]').toggleClass('glyphicon-triangle-bottom','glyphicon-triangle-bottom');
          $(div).children('span[id*="s"]').toggleClass('glyphicon-triangle-right','glyphicon-triangle-right');
        }
      },
      save(){
        let foo = $('.grandFather');
        let grandFatherDiv = [];
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
            grandFatherInputObject.storeCategorySecond = [];
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
                fatherInputObject.storeCategoryThird = [];
                let foo = $(obj).children('.son');
                let sonDiv = [];
                for(let prop in foo){
                  if(prop > -1){
                    sonDiv.push(foo[prop]);
                  }
                  else{
                    break;
                  }
                }
                let sonInputObject = sonDiv.map(function(obj){
                  let sonInputObject = {};
                  let sInput = $(obj).children('.sonInput').val();                
                  sonInputObject.objectId = $(obj).children('.sonInput').attr('id');
                  sonInputObject.name = sInput;
                  return sonInputObject;
                })
                fatherInputObject.storeCategoryThird = sonInputObject;
                return fatherInputObject;
            });
            grandFatherInputObject.storeCategorySecond = fatherInputObject;
            return grandFatherInputObject;
        }); 
        let obj = {};
        obj.StoreCategoryFirst = [];
        obj.StoreCategoryFirst = grandFatherInputObject;
        swal({
          title: "你确定更新库存分类吗?",
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
            url: '/Product/CreateStoreCategory/',
            headers: {
              'X-CSRFToken': $('input[name="csrfmiddlewaretoken"]').prop('value')
            },
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            data: JSON.stringify(obj),
            success: function (data) {
              swal("库存分类已经更新为最新版");
            },
            error: function(XMLHttpRequest, textStatus, errorThrown) {
              swal("库存分类更新失败");
            },           
          });
        });
      },
    },
  }
</script>

<style>
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
    margin-right: 300px;
    font-size: large;
  }
  .oprate{
    background-color: burlywood;
  }
  .fatherInput{
    position: relative;
    left: 50px;
  }
  .sonInput{
    position: relative;
    left: 100px;
  }
  .thirdAdd{
    position: relative;
    left: 100px;
  }
  .secondAdd{
    position: relative;
    left:50px;
  }
  .directLine{
    width: 30px;
    height: 20px;
    display: inline-block;
    border-bottom: 2px solid;
    border-left: 2px solid;
    position: absolute;
    left: 10px;
  }
  .father .glyphicon-triangle-bottom,.father .glyphicon-triangle-right{
    position:relative;
    left: 45px;
  }
  .directLine.add{
    left: 55px;
  }
  .son .glyphicon-triangle-bottom,.son .glyphicon-triangle-right{
    position:relative;
    left:95px;
  }
  .remove{
    position: relative;
    left: 440px;
    top: 5px;
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
</style>

