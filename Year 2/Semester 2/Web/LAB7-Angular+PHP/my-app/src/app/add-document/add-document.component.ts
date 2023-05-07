import { Component, OnInit } from '@angular/core';
import { FormArray, FormBuilder, FormControl, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { DocumentsService } from '../documents.service';
@Component({
  selector: 'app-add-document',
  templateUrl: './add-document.component.html',
  styleUrls: ['./add-document.component.sass']
})
export class AddDocumentComponent{
  addForm:any;

  vals = ''
  data= this.vals.split(',');

  constructor(
    private formBuilder: FormBuilder,
    private router: Router,
    private documentService:DocumentsService
  ) {

    this.addForm = this.formBuilder.group({
        author: ['', Validators.required],
        title: ['', [Validators.required, Validators.maxLength(20)]],
        pages: ['', [Validators.required, Validators.maxLength(20)]] , // TODO INT !!
        types: ['', [Validators.required, Validators.maxLength(20)]] ,
        format: ['', Validators.required],
      }
    )
  }

  onSubmit(){
    this.documentService.createDocument(this.addForm.value).subscribe(
      (data:any)=>{
        this.router.navigate(['/']);
      },
      error => {
        alert(error);
      });
  }
}
