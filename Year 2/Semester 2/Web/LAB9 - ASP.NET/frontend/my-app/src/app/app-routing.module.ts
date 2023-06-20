import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {DocumentAddEditComponent} from "./document-add-edit/document-add-edit.component";
import {CommonModule} from "@angular/common";
import {LogInComponent} from "./log-in/log-in.component";
import {RegisterComponent} from "./register/register.component";
import {DocumentsComponent} from "./documents/documents.component";

const routes: Routes = [
  { path: '', pathMatch: 'full', redirectTo: 'login' },
  { path: 'login', component: LogInComponent },
  { path: 'register', component: RegisterComponent },
  { path: 'documents', component: DocumentsComponent},
  ];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
