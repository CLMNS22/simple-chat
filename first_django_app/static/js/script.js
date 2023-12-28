// async function sendMessage() {
//     let fd = new FormData();
//     let csrf_token = '{{ csrf_token }}'
//     fd.append('messageText', messageField.value);
//     fd.append('csrfmiddlewaretoken', csrf_token);

//     try {
//         const currentTime = getCurrentDateTime();
//         messageContainer.innerHTML += `
//         <div id="deleteMessage">
//             <span class="color-grey"> [${currentTime}] </span>{{request.user.first_name}}:<i class="color-grey"> ${messageField.value} </i> <br>
//         </div>
//         `;
//         let response = await fetch('/chat/', {
//             method: 'POST',
//             body: fd
//         });

//         if (!response.ok) {
//             throw new Error(response.statusText)
//         }

//         document.getElementById('deleteMessage').remove();
//         messageContainer.innerHTML += `
//         <div id="deleteMessage">
//             <span class="color-grey"> [${currentTime}] </span>{{request.user.first_name}}:<i> ${messageField.value} </i> <br>
//         </div>
//         `;
//     } catch (error) {
//         console.log(error);
//     }
// }

// function getCurrentDateTime() {
//     const currentDate = new Date();

//     const options = {
//         year: 'numeric',
//         month: 'short',
//         day: 'numeric',
//         hour: 'numeric',
//         minute: 'numeric'
//     };

//     const dateTimeFormatter = new Intl.DateTimeFormat('de-DE', options);
//     const formattedDateTime = dateTimeFormatter.format(currentDate);

//     return formattedDateTime;
// }