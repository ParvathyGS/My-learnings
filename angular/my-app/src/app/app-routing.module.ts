import { NgModule }             from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PostsComponent } from './posts/posts.component';
import { TestappComponent } from './testapp/testapp.component';

const routes: Routes = [
  { path: 'posts', component: PostsComponent },
  { path: 'test', component: TestappComponent }
];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})


export class AppRoutingModule {}