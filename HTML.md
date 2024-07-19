# HTML File
- **HTML:** Defines the structure and content of the webpage 网页结构和内容
- **CCS :** Defines the style of the webpage 确定风格
- **JavaScript:** Define the interaction between user and webpage网页交互方式

### Here is a typical HTML
```HTML
<!DOCTYPE HTML> # Head: telling this is a HTML file
<html> # Starter label
    <body> # Main element
        <h1> This is a header </h1> # inside the body, they are brother element 
        <p> This is text </p>
    </body>
</html> # End label
```
Every content in the <> is a label of the HTML label. The content between starter and end label is on html label. 


## Encode
`<meta charset="UTF-8">` for setting the way web encode.(for chinese) 

## Label of HTML

- `<h1>` h follow by number represent the headers 
- `<p>` represent the text. 
  - `<br>` line feed.
  - `<b>` bold.
  - `<i>` italic.
  - `<u>` underline
- `<img src = "YOUR_IMAGE_LINK" width="500px">` upload image
- `<a href="YOUR_LINK", target="_self">LINK_LABEL</a>`Add link. target `"_self"` is to open the link in the current window, `"_blank"` is using a new window to open.
- Container     
  - `<div style="CONTAINER">` For a line
  - `<span style="CONTAINER">` For element in the line
- List 
  - `<ol> <li>1</li> </ol>` with order 
  - `<ul> <li>1</li> </ul>`Without order 
- Table
  ```HTML
    <table border="1"> <!--Table border type-->
        <!--The head of the table-->
        <thead>
           <tr>
            </tr> 
        </thead>
        <!--The body of the table-->
        <tbody>
            <tr>    <!--table row-->
                <td>111</td> <!--table data-->
                <td>222</td>
            </tr>

        <tbody>
    </table>
  ```
- Class
  - Can be apply to all label. Help with grouping.