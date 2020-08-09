import { Component, OnInit } from '@angular/core';
import { QuestionsService } from '../questions.service';
import { Answer, Question } from '../question';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-editquestion',
  templateUrl: './editquestion.component.html',
  styleUrls: ['./editquestion.component.css']
})
export class EditquestionComponent implements OnInit {

  constructor(
    private questionService : QuestionsService,
    private route: ActivatedRoute,
  ) { }

  ngOnInit() {
  }

question : Question;

editQuestion(question : Question) {
  console.log("abc");
  const id = +this.route.snapshot.paramMap.get('id');
  console.log(id);
  this.questionService.EditQuestion(question,id).subscribe(res => this.question = res);
}
}
