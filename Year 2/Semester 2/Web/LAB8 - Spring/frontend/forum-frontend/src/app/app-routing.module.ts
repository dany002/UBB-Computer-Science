import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {LogInComponent} from "./log-in/log-in.component";
import {RegisterComponent} from "./register/register.component";
import {TopicsComponent} from "./topics/topics.component";
import {TopicDetailsComponent} from "./topic-details/topic-details.component";

const routes: Routes = [
  { path: '', pathMatch: 'full', redirectTo: 'login' },
  { path: 'login', component: LogInComponent },
  { path: 'register', component: RegisterComponent },
  { path: 'topics', component: TopicsComponent},
  { path: 'topic-details/:id', component: TopicDetailsComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
