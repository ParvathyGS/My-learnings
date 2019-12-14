import { Component, OnInit } from '@angular/core';
import { ActivatedRoute,Router } from '@angular/router';
import { Location } from '@angular/common';
import { User } from '../user';
import { UserService } from '../user.service';
import { MessageService } from '../message.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  constructor(
    private route:ActivatedRoute,
    private location:Location,
    private userService: UserService,
    private router: Router,
    private messageService: MessageService,
  ) { }

  ngOnInit() {
  }

  data: Object = {};


  onSubmit(user_details:any) {
    this.messageService.add('Login Successful');
    this.userService.loginAction(user_details).subscribe(
      res =>
        {
          localStorage.setItem("userToken",res.token)
          // localStorage.setItem("userName",res.user.name);
          // if(res.token){
          //   this.router.navigateByUrl("question");
          // }else{
          //   this.router.navigateByUrl("/login");
          // }
        }
    ); 
      }
}
