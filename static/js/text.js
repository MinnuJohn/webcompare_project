
// $(function () {

//     $(".progress").each(function () {
  
//       var value = $(this).attr('data-value');
//       var left = $(this).find('.progress-left .progress-bar');
//       var right = $(this).find('.progress-right .progress-bar');
  
//       if (value > 0) {
//         if (value <= 50) {
//           right.css('transform', 'rotate(' + percentageToDegrees(value) + 'deg)')
//         } else {
//           right.css('transform', 'rotate(180deg)')
//           left.css('transform', 'rotate(' + percentageToDegrees(value - 50) + 'deg)')
//         }
//       }
  
//     })
  
//     function percentageToDegrees(percentage) {
  
//       return percentage / 100 * 360
  
//     }
  
//   });
  
  
  function compareSimilarity(evt) {
    evt.preventDefault();
  
    // Retrieve values from the input fields
    const text1 = document.querySelector('#text1').value;
    const text2 = document.querySelector('#text2').value;
    
    // Send a POST request to the server to compare similarity
    fetch('/processtext', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        text1: text1,
        text2: text2,
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log(data)
        // Display the similarity result on the page
        document.querySelector('#result').textContent = `Similarity: ${data.similar}`;
      });
  }
  
  // Add event listener to the form
  const form = document.querySelector('#comparison-form');
  form.addEventListener('submit', compareSimilarity);