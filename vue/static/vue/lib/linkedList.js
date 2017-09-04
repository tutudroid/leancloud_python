export const config = function(code,name,url){
  this.code = code;
  this.name = name;
  this.url = url;
}

export const linkedList = function(){

 var Node = function (element) {　　　　　　　　//新元素构造
            this.element = element;
            this.next = null;
        };
        this.length = 0;
        var head = null;

        this.append = function (element) {
            var node = new Node(element);　　　　　　　　//构造新的元素节点
            var current;
            if (head === null) {　　　　　　　　　　　　　//头节点为空时  当前结点作为头节点
                head = node;
            } else {
                current = head;　　　　　　　　　　　　　　
                while (current.next) {　　　　　　　　　　//遍历，直到节点的next为null时停止循环，当前节点为尾节点
                    current = current.next;
                }
                current.next = node;　　　　　　　　　　　　//将尾节点指向新的元素，新元素作为尾节点
            }           
            this.length++;　　　　　　　　　　　　　　　　　　　　//更新链表长度
        };
        this.removeAt = function (position) {
            if (position > -1 && position < this.length) {
                var current = head;
                var index = 0;
                var previous;
                if (position == 0) {
                    head = current.next;
                } else {
                    while (index++ < position) {
                        previous = current;
                        current = current.next;
                    }
                    previous.next = current.next;
                }
                this.length--;
                return current.element;
            } else {
                return null;
            }
        };
	this.getConfig = function(pos) {
	
	    if(pos > -1 && pos < this.length ){
	    
              var current = head;
              while( pos > 0 ){
		pos--;
	        current = current.next;
	      }
	    
	      return current.element;


	    }else{
	      return null;
	    }

	};
        this.toString = function () {
            var current = head;
            var string = '';
            while (current) {
                string += ',' + current.element;
                current = current.next;
            }
            return string;
        };

}
