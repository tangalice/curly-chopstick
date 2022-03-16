## Create Task
Snippets:
```
if (!gameOver && row == height) {
                gameOver = true;
                document.getElementById("answer").innerText = word;
            }
```
```
if ("KeyA" <= e.code && e.code <= "KeyZ") {
                if (col < width) {
                    let currTile = document.getElementById(row.toString() + '-' + col.toString());
                    if (currTile.innerText == "") {
                        currTile.innerText = e.code[3];
                        col += 1;
                    }
                }
            }
```
[Create Task Description](https://github.com/samayass/flask_portfolio/wiki/Create-Task-Plan:-Samaya-&-Alice) <br>
[Create Task Runtime](http://studyowl.tk:8080/test/) <br>
[Create Task Code](https://github.com/samayass/flask_portfolio/blob/main/templates/test.html)
