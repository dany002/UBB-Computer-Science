import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {ListDocumentsComponent} from "./list-documents/list-documents.component";
import {AddDocumentComponent} from "./add-document/add-document.component";
import {EditDocumentComponent} from "./edit-document/edit-document.component";
import {CommonModule} from "@angular/common";

const routes: Routes = [
  { path: '', component: ListDocumentsComponent, pathMatch: 'full' },
  { path: 'add-student', component: AddDocumentComponent },
  { path: 'edit/:id', component: EditDocumentComponent },
];

@NgModule({
  imports: [
    CommonModule,
    RouterModule.forRoot(routes)
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
