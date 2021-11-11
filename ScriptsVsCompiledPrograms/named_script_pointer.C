int named_script_pointer(){
	TH1F *h = new TH1F("myHist", "histogram", 10,0,10);
	for(int i=0; i<h->GetNbinsX(); i++) h->SetBinContent(i,2*i);
	h->Draw();
	h->Print();
	return 0;
}
