import { Component, OnInit } from '@angular/core';
import { Question,Answer } from '../question';
import { User } from '../user';
import { QuestionsService } from '../questions.service';
import { ActivatedRoute } from '@angular/router';
import { MessageService } from '../message.service';

@Component({
  selector: 'app-showquestion',
  templateUrl: './showquestion.component.html',
  styleUrls: ['./showquestion.component.css']
})
export class ShowquestionComponent implements OnInit {



  constructor(
    private questionService:QuestionsService,
    private route: ActivatedRoute,
    private messageService:MessageService,
   
  ) {}
    

  ngOnInit() {
    this.Showquestion();
  }

  question : Question;
  
  Showquestion() {
    const id = +this.route.snapshot.paramMap.get('id');
    this.questionService.showQuestion(id).subscribe(
      res => {
      this.question = res,
      console.log(res);
      // localStorage.setItem("QuestionId",res.answers.user_id);
      // var input = document.getElementById('AnsuserId');
      // console.log(input);
      }
    );
}

likeCount : number = 0;
dislikeCount : number = 0;
// question : Question;

likeQuestion() {
  const id = +this.route.snapshot.paramMap.get('id');
  this.likeCount = this.likeCount+1;
  console.log(id);
  console.log(this.likeCount);
  this.questionService.LikeQuestion(this.likeCount,id).subscribe(res => 
    console.log(res));
}

dislikeQuestion() {
  const id = +this.route.snapshot.paramMap.get('id');
  this.dislikeCount = this.dislikeCount+1;
  console.log(id);
  console.log(this.dislikeCount);
  this.questionService.DislikeQuestion(this.dislikeCount,id).subscribe(res => 
    console.log(res)

    );
}
}
