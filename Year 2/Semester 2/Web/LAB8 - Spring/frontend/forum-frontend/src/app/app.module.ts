import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import {FormsModule, ReactiveFormsModule} from "@angular/forms";
import {MatButtonModule} from '@angular/material/button';
import {MatInputModule} from '@angular/material/input';
import {BrowserAnimationsModule} from "@angular/platform-browser/animations";
import {MatToolbarModule} from "@angular/material/toolbar";

import {FlexLayoutModule} from "@angular/flex-layout";
import {MatCardModule} from "@angular/material/card";
import { RegisterComponent } from './register/register.component';
import {MatSelectModule} from "@angular/material/select";
import {MatFormFieldModule} from "@angular/material/form-field";
import {LogInComponent} from "./log-in/log-in.component";
import {HttpClientModule} from "@angular/common/http";
import { TopicsComponent } from './topics/topics.component';
import {MatTableModule} from "@angular/material/table";
import {MatSortModule} from "@angular/material/sort";
import {MatIconModule} from "@angular/material/icon";
import {MatPaginatorModule} from "@angular/material/paginator";
import {MatDialogModule} from "@angular/material/dialog";
import { TopicDetailsComponent } from './topic-details/topic-details.component';
import {MatSnackBar, MatSnackBarModule} from "@angular/material/snack-bar";
import { ConfirmationDialogComponent } from './confirmation-dialog/confirmation-dialog.component';


@NgModule({
  declarations: [
    AppComponent,
    LogInComponent,
    RegisterComponent,
    TopicsComponent,
    TopicDetailsComponent,
    ConfirmationDialogComponent,

  ],
    imports: [
        BrowserModule,
        AppRoutingModule,
        FormsModule,
        MatButtonModule,
        MatInputModule,
        BrowserAnimationsModule,
        MatToolbarModule,
        FlexLayoutModule,
        ReactiveFormsModule,
        MatCardModule,
        MatSelectModule,
        MatFormFieldModule,
        HttpClientModule,
        MatTableModule,
        MatSortModule,
        MatIconModule,
        MatPaginatorModule,
        MatDialogModule,
        MatSnackBarModule
    ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
