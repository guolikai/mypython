//alert('guolikai郭立凯');
//单行注释
/*
多行注释
*/
//name1 = "glk1" 全局变量 window.name1 = "glk1"
//var name2 = "glk2" 局部变量
Foo('GuoLikai',"WuDanxia")
function Foo(name){
    var arg2 = arguments[1]
    console.log(name);
    console.log(arg2);
    return "return value";
}
//默认参数
//console.log打印
name = "HaoYiwei"
Fun()
function Fun(){
    console.log(name);
}
//自执行函数,没有函数名，形参在第一个（）内；；实参在第二个（）内；
//(function(){console.log('自执行函数:value');})()
(function(name3){console.log(name3);})('value')
var arry = [1,2,3,4];
console.log(arry);
arry.push(5);
console.log(arry);
arry.unshift('glk')
console.log(arry);
arry.splice(4,0,"wdx")
console.log(arry);
arry.splice(100,0,"wdx100")
console.log(arry)
arry[99]='love';
console.log(arry[97])
console.log(arry[98])
console.log(arry[99])
console.log(arry[100])
console.log(arry[7])



for (var i in arry){console.log(i)} //循环的是key
dict = {'name':'guolikai','age':27};
for (var item in dict){console.log(dict[item])};

for(var i=0;i<arry.length;i++){
     console.log(dict[i]);
}
for(var i=0;i<dict.length;i++){
     console.log(dict[i]);
}
