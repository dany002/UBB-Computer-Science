import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { AddDocumentComponent } from './add-document/add-document.component';
import {ReactiveFormsModule} from "@angular/forms";
import { EditDocumentComponent } from './edit-document/edit-document.component';
import { ListDocumentsComponent } from './list-documents/list-documents.component';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
@NgModule({
  declarations: [
    AppComponent,
    AddDocumentComponent,
    EditDocumentComponent,
    ListDocumentsComponent
  ],
    imports: [
        BrowserModule,
        AppRoutingModule,
        ReactiveFormsModule,
        FormsModule,
        HttpClientModule
    ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
