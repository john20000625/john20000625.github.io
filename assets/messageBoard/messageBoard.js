        var text = document.querySelector('textarea');
        var btn = document.querySelector('button');
        var ul = document.querySelector('ul');
        btn.onclick = function () {
            if (text.value == '') {
                alert('不能给空的留言哟')
                return false;
            } else {
                //创建元素
                var li = document.createElement('li');
                li.innerHTML = text.value + "<a href='javascript: ;'> 删除</a>";//javascript:;阻止链接跳转
                ul.insertBefore(li, ul.children[0]);//在当前元素前生成新的li
                text.value = '';
                //删除元素  删除的是当前连接a  需要删除的是他父亲li
                var as = document.querySelectorAll('a');
                for (var i = 0; i < as.length; i++) {
                    as[i].onclick = function () {
                        //node.removechildren(children)  删除的是li  当前a所在的li  this.parentnode;
                        ul.removeChild(this.parentNode);
                    }
                }
            }
        }
