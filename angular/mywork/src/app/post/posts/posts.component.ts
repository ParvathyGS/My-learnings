import { Component, OnInit } from '@angular/core';
import * as $ from 'jquery';
declare var $: any;
// @import 'path/to/css/posts.component.css';

import { Post } from '../post';
import { PostService } from '../post.service';

@Component({
  selector: 'app-posts',
  templateUrl: './posts.component.html',
  styleUrls: ['./posts.component.css']
})

export class PostsComponent implements OnInit {

  constructor(private postService: PostService) { }

  ngOnInit() {
    this.getPost();
  }

  posts:Post[];

  getPost(){
    this.postService.getPosts().subscribe(posts => this.posts = posts);
  }

  add(title:string, body:string):void {
    let newPost = new Post;
    newPost.title = title;
    newPost.body = body;
    this.postService.addPost(newPost).subscribe(post => this.posts.push(post));
  }

  pushPost(post:Post){
    this.posts.push(post);
    $("#addPostModal").modal("hide");
  }
}
