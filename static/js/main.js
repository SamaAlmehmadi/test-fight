/*const contactApi = [{  // the api from server
   name: 'Amer Omar ',
    phone: '01152306375'
},
{
    name: 'Ahmed',
    phone: '01152306374'
}, 
{
    name: 'Mohamed',
    phone: '01152306373'
},
{
    name: 'Hafez',
    phone: '01152306373'
},
]; */


function creatcontactList (name, phone) {
    const listBox = document.getElementById('contactList');
    const Li = document.createElement('li');
    Li.classList = 'list-group-item container';
    Li.id = phone;
    Li.innerHTML = `<div class="row"> <div class="col-3 name"><span class="icon">${name[0]}${name[1]}</span><p>${name}</p> </div><div class="col-4 phone">${phone}</div><div class="col-4 icons"></i><i class="fa fa-trash" id="conicon" onclick="removeContact('${phone}')" aria-hidden="true"></i></div></div>`;
    listBox.appendChild(Li)
}
const removeContact = (phone) => {
    const contact = document.getElementById(`${phone}`);
    if (confirm('remove this contact ?')) {
        contact.remove();
    }
}
/*contactApi.forEach(c => {
    creatcontactList(c.name, c.phone);
})*/

for (let i =0 ; i < 4 ; i++ ) {
    
	creatcontactList(contactApi[i].name, contactApi[i].phone);

}

const check = document.getElementById('check');
check.addEventListener("click", ()=> {
if (contactApi[3]) {
	if (confirm("You Can not add more than 4 Contact ")){
	location.reload()
	} else {
		location.reload()
		}
	
} /*else { 
const checkless = document.getElementById('checkless')
checkless.submit();
} */
})

