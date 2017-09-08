<template>
    <div class="searchStockCategoryVue">
		<form class="form-inline">
		  <div class="form-group" @click="clickFirst()">
		    <label for="first">一级分类</label>
		    <select class="form-control" id="first" v-model="firstCate"  @change="changeSecond()">
			    <option disabled value="">请选择一级分类</option>
				<option disabled value="">--------</option>
				<option disabled value="">--------</option>
		    </select>
		  </div>
		  <div class="form-group">
			    <label for="second">二级分类</label>
			    <select class="form-control" id="second" v-model="secondCate" @change="changeThird()">
			        <option disabled value="">必须先选择一级分类</option>
					<option value="">"不选"</option>
			    </select>
		  </div>
		  <div class="form-group">
		    <label for="third">三级分类</label>
		    <select class="form-control" id="third" v-model="thirdCate">
		        <option disabled value="">必须先选择二级分类</option>
				<option value="">"不选"</option>
		    </select>
		  </div>
		  <button type="submit" class="btn btn-default">搜索</button>
		</form> 
    </div>
</template>

<script>
  export default{

    data:function(){
      return {
        first:[],
		second:[],
		firstCate:"",
		secondCate:"",
		thirdCate:""
      }
    },   
    props:['storecategory'],
    methods:{      
        clickFirst(){	
		  let firstName = [];
		  let _this = this;
		  let addedFirst = "";
		  let addedStuff = $('.addedFirst');
	      if(addedStuff.hasClass('addedFirst')){

		  }else{
		  this.storeCategory.forEach(
		    function(item,index){
		      firstName[index] = item.name;
		      let secondName = [];
		      let secondCategory = item.value;
		      secondCategory.forEach(
		        function(item,index){
			  	secondName[index] = item;
			  });
		      _this.second[index] = secondName;	      
		      addedFirst += "<option class='addedFirst' value='"+index+"'>"+item.name+"</option>"		    
		  });
		  this.first = firstName;
		  $(addedFirst).appendTo('#first');
		  } 
		},
		changeSecond(){
		  let addedStuff = $('.addedSecond');
		  if(addedStuff.hasClass('addedSecond')){
		    $( ".addedSecond" ).remove();
		  }
	      let secondCate = this.firstCate;
		  let secondCates = this.second[secondCate];
		  let addedSecond = "";
		  secondCates.forEach(
		    function(item,index){
		      addedSecond += "<option class='addedSecond' value='"+index+"'>"+item.name+"</option>";
		  });
		  $(addedSecond).appendTo('#second');
		  if(this.secondCate != ""){
		    this.changeThird();
		  }	        
       },
       changeThird(){
		  let addedStuff = $('.addedThird');
		  if(addedStuff.hasClass('addedThird')){
		    $( ".addedThird" ).remove();
		  }
	      let secondCate = this.firstCate;
		  if(this.secondCate != ""){
			  let thirdCate = this.secondCate;
			  let first = this.second[secondCate];
			  let second = first[thirdCate];
		      let thirdCates = second.value;
			  let addedThird = "";
			  thirdCates.forEach(
			    function(item){
			      addedThird += "<option class='addedThird' value='"+item.id+"'>"+item.name+"</option>";
			    }
			  );
			 $(addedThird).appendTo('#third');
		  }        
       },    
    },

}
</script>

<style>
select#first {
  padding: 0 50px;
}
</style>
