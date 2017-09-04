<template>
 <div class="editStockCategory">
  <h2 @click="addFirstHtml(1)" class="addBtn"><span class="glyphicon glyphicon-plus"></span>加一级分类</h2>
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
      addFirst(){
        let first = new Category();
	let second = new Category();
	let third = new Category();
	first.children.push(second);
	second.childre.push(third);
	this.first.push(first);
	this.second.push(second);
	this.third.push(third);
	this.index[this.count] = [this.firstCount,this.secondCount,this.thirdCount];
	this.count++;
	this.firstCount++;
	this.secondCount++;
	this.thirdCount++;
	this.addFirstHtml();
      },
      addSecond(e){
        let index = index[e.currentTarget.parentElement.index][0];
	let first = this.first[index]
        let second = new Category();
	let third = new Category();
	first.children.push(second);
	second.children.push(third);
	this.index[this.count] = [index,this.secondCount,this.thirdCount];
	this.count++;
	this.secondCount++;
	this.thirdCount++;

      },
      addThird(e){
        let firstIndex = index[e.currentTarget.parentElement.index][0]
        let index = index[e.currentTarget.parentElement.index][1];
	let second = this.second[index];
	let third = new Category();
	second.children.push(third);
	this.index[this.count] = [firstIndex,index,this.thirdCount];
	this.count++;
	this.thirdCount++;
      },
      addFirstHtml(index){
        let _this = this; 
        let firstHtml = "<div  index='"+index+"'class='grandFather mainContent'><input type='text' class='grandFatherInput'><span class='glyphicon glyphicon-remove remove link'></span><hr><div index='"+index+"'class='father'><span class='directLine'></span><input type='text' class='fatherInput'><span class='glyphicon glyphicon-remove remove link'></span><hr><div index='"+index+"'class='son'><span class='directLine add'></span><input type='text' class='sonInput'><span class='glyphicon glyphicon-remove remove link'></span><hr></div><div class='addThird'><span class='directLine add'></span><button class='btn btn-primary thirdAdd'>添加三级子分类</button><hr></div></div><div class='addSecond'><span class='directLine'></span><button class='btn btn-primary secondAdd'>添加二级子分类</button><hr></div></div>";
	$(firstHtml).appendTo('.cateContent');
	$('.remove').bind('click',function(event){
	  _this.deleteHtml(event);
	});
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
  .directLine.add{
    left: 55px;
  }
  .remove{
    position: relative;
    left: 455px;
    top: 5px;
  }
  .mainContent{
    position: relative;
    left: 40px;
    top: 10px;
  }
</style>
