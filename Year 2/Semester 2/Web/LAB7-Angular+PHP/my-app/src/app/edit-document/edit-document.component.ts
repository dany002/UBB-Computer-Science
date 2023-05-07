import { Component, OnInit } from '@angular/core';
import { FormArray, FormBuilder, FormControl, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { DocumentsService } from '../documents.service';
@Component({
  selector: 'app-edit-document',
  templateUrl: './edit-document.component.html',
  styleUrls: ['./edit-document.component.sass']
})
export class EditDocumentComponent implements OnInit{
  addForm:any;
  vals = ''
  data= this.vals.split(',');
  document_id: any;

  constructor(
    private formBuilder: FormBuilder,
    private router: Router,
    private documentService:DocumentsService,
    private url:ActivatedRoute
  ) {
    this.addForm = this.formBuilder.group({
        id:[],
        author: ['', Validators.required],
        title: ['', [Validators.required, Validators.maxLength(20)]],
        pages: ['', [Validators.required, Validators.maxLength(20)]] , // TODO INT !!
        types: ['', [Validators.required, Validators.maxLength(20)]] ,
        format: ['', Validators.required],
      }
    )
  }

  ngOnInit(): void {
    this.document_id = this.url.snapshot.params['id'];
    if (this.document_id>0) {
      this.documentService.getSingleDocument(this.document_id).subscribe((
        (data:any)=>{
          this.addForm.patchValue(data.data);
        }
      ))
    }
  }
  onEdit(){
    this.documentService.editDocument(this.addForm.value).subscribe(
      (data:any)=>{
        console.log(data);
        this.router.navigate(['/']);
      },
      error => {
        alert(error);
      });
  }
}
