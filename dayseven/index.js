



let btn= document.querySelector("#btn");
let emptyListContainer= document.querySelector("#emptyListContainer");


btn.addEventListener("click",action);

function action(){
     let inputField= document.querySelector(".inputField");
     let getValue= inputField.value.trim()
   
       if (getValue!=""){
            
            let list = document.createElement("li")
            let checkbox = document.createElement("input");
            checkbox.type="checkbox"
            list.appendChild(checkbox)
            list.append(getValue)
            let del = document.createElement("button")
            del.textContent="delete"
            list.appendChild(del)
            
            del.addEventListener("click",function(){
                list.remove()
            })
            
            
            emptyListContainer.appendChild(list)
            inputField.value=""
            
       }
    

   

   

    



}