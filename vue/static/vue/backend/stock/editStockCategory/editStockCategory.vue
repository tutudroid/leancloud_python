<template>
 <div class="editStockCategory">
  <h2 @click="addFirstHtml()" class="addBtn"><span class="glyphicon glyphicon-plus"></span>加一级分类</h2>
  <div class="cateContent">
    <h3 class="save link">保存</h3>
    <h3 class="oprate"><span class="title">分类名称</span><span class="title">--</span><span class="title">操作</span></h3>
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
     }
    
    },
    methods:{
      addFirstHtml(){
        let _this = this; 
        let firstHtml = "<div class='grandFather mainContent'><span class='glyphicon glyphicon-triangle-bottom'></span><input type='text' class='grandFatherInput'><span class='glyphicon glyphicon-remove remove link'></span><hr><div class='father'><span class='directLine'></span><span class='glyphicon glyphicon-triangle-bottom'></span><input type='text' class='fatherInput'><span class='glyphicon glyphicon-remove remove link'></span><hr><div class='son'><span class='directLine add'></span><span class='glyphicon glyphicon-triangle-bottom'></span><input type='text' class='sonInput'><span class='glyphicon glyphicon-remove remove link'></span><hr></div><div class='addThird'><span class='directLine add'></span><button class='btn btn-primary thirdAdd'>添加三级子分类</button><hr></div></div><div class='addSecond'><span class='directLine'></span><button class='btn btn-primary secondAdd'>加二级子分类</button><hr style='border-top:3px solid #a00404'></div></div>";
	$(firstHtml).appendTo('.cateContent');
	$('.remove').bind('click',function(event){
	  _this.deleteHtml(event);
	});
	$('.secondAdd').bind('click',function(event){
	  _this.addSecondHtml(event);
	});
	$('.thirdAdd').bind('click',function(event){
	  _this.addThirdHtml(event);
	});
      },
      addSecondHtml(event){
        let targetSecond = $(event.currentTarget).parent().parent();
	let button = $(event.currentTarget).parent();
	let secondHtml = '<div class="father"><span class="directLine"></span><span class="glyphicon glyphicon-triangle-bottom"></span><input type="text" class="fatherInput"><span class="glyphicon glyphicon-remove remove link"></span><hr><div class="son"><span class="directLine add"></span><span class="glyphicon glyphicon-triangle-bottom"></span><input type="text" class="sonInput"><span class="glyphicon glyphicon-remove remove link"></span><hr></div><div class="addThird"><span class="directLine add"></span><button class="btn btn-primary thirdAdd">添加三级子分类</button><hr></div></div>';
	$(secondHtml).appendTo(targetSecond);
	$(button).appendTo(targetSecond);
      },
      addThirdHtml(event){
        let targetThird = $(event.currentTarget).parent().parent();
	let thirdHtml = '<div class="son"><span class="directLine add"></span><span class="glyphicon glyphicon-triangle-bottom"></span><input type="text" class="sonInput"><span class="glyphicon glyphicon-remove remove link"></span><hr></div>';
	$(thirdHtml).appendTo(targetThird);
      },
      deleteHtml(e){
        console.log(e.currentTarget.parentElement.getAttributeNode('index').value);
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
  .father .glyphicon-triangle-bottom{
    position:relative;
    left: 45px;
  }
  .directLine.add{
    left: 55px;
  }
  .son .glyphicon-triangle-bottom{
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
</style>
