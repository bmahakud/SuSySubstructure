#!/usr/bin/python
import ROOT
ROOT.gROOT.ProcessLine(".L ~/tdrstyle.C");
ROOT.setTDRStyle();
ROOT.gStyle.SetPadTopMargin(0.09);
ROOT.gStyle.SetPadLeftMargin(0.16);
ROOT.gStyle.SetPadRightMargin(0.06);
ROOT.gStyle.SetPadBottomMargin(0.35);
ROOT.gStyle.SetPalette(1);
ROOT.gStyle.SetErrorX(0.5);

## ------------------------------------------------------------

class binContainer:
	
	def __init__(self, yields, cardname):	
		
		# sig, qcd1, ttbar, w+jets, z+jets, qcd2
		self.yields = [float(yields[0]),float(yields[1])+float(yields[5]),float(yields[2]),float(yields[3]),float(yields[4])];
		self.cn     = cardname;
		self.limit  = 1;

	def getYields(self): return self.yields;

## ------------------------------------------------------------

class WorkingPointContainer:

    def __init__(self, mgluino, mlsp, anatype):
    	
    	self.mGo = mgluino;
    	self.mLSP = mlsp;
        self.ncategoriesNames = ["sig","QCD","ttbar","w+jets","z+jets"];
    	self.anatype = anatype;

        # bin labels
        self.nbinsLabels = [];

        if self.anatype == "SMJ":
	    #self.nbinsLabels.append("smj400,mht150,nj3-5");
	    #self.nbinsLabels.append("smj400,mht150,nj6-7");
	    #self.nbinsLabels.append("smj400,mht150,nj8-99");
            self.nbinsLabels.append("smj0,mht200,nj3-5");
            self.nbinsLabels.append("smj0,mht300,nj3-5");
            self.nbinsLabels.append("smj0,mht450,nj3-5");
            self.nbinsLabels.append("smj0,mht600,nj3-5");
            self.nbinsLabels.append("smj200,mht200,nj3-5");
            self.nbinsLabels.append("smj200,mht300,nj3-5");
            self.nbinsLabels.append("smj200,mht450,nj3-5");
            self.nbinsLabels.append("smj200,mht600,nj3-5");
            self.nbinsLabels.append("smj400,mht200,nj3-5");
            self.nbinsLabels.append("smj400,mht300,nj3-5");
            self.nbinsLabels.append("smj400,mht450,nj3-5");
            self.nbinsLabels.append("smj400,mht600,nj3-5");
            self.nbinsLabels.append("smj600,mht200,nj3-5");
            self.nbinsLabels.append("smj600,mht300,nj3-5");
            self.nbinsLabels.append("smj600,mht450,nj3-5");
            self.nbinsLabels.append("smj800,mht200,nj3-5");
            self.nbinsLabels.append("smj800,mht300,nj3-5");
            
            self.nbinsLabels.append("smj0,mht200,nj6-7");
            self.nbinsLabels.append("smj0,mht300,nj6-7");
            self.nbinsLabels.append("smj0,mht450,nj6-7");
            self.nbinsLabels.append("smj200,mht200,nj6-7");
            self.nbinsLabels.append("smj200,mht300,nj6-7");
            self.nbinsLabels.append("smj200,mht450,nj6-7");
            self.nbinsLabels.append("smj400,mht200,nj6-7");
            self.nbinsLabels.append("smj400,mht300,nj6-7");
            self.nbinsLabels.append("smj400,mht450,nj6-7");
            self.nbinsLabels.append("smj600,mht200,nj6-7");
            self.nbinsLabels.append("smj600,mht300,nj6-7");
            self.nbinsLabels.append("smj600,mht450,nj6-7");
            self.nbinsLabels.append("smj800,mht200,nj6-7");
            self.nbinsLabels.append("smj800,mht300,nj6-7");

            self.nbinsLabels.append("smj0,mht200,nj8-99");
            self.nbinsLabels.append("smj200,mht200,nj8-99");
            self.nbinsLabels.append("smj400,mht200,nj8-99");
            self.nbinsLabels.append("smj600,mht200,nj8-99");
            self.nbinsLabels.append("smj800,mht200,nj8-99");
        
        if self.anatype == "Classic":
            self.nbinsLabels.append("ht500,mht200,nj3-5");
            self.nbinsLabels.append("ht500,mht300,nj3-5");
            self.nbinsLabels.append("ht500,mht450,nj3-5");
            self.nbinsLabels.append("ht500,mht600,nj3-5");
            self.nbinsLabels.append("ht800,mht200,nj3-5");
            self.nbinsLabels.append("ht800,mht300,nj3-5");
            self.nbinsLabels.append("ht800,mht450,nj3-5");
            self.nbinsLabels.append("ht800,mht600,nj3-5");
            self.nbinsLabels.append("ht1000,mht200,nj3-5");
            self.nbinsLabels.append("ht1000,mht300,nj3-5");
            self.nbinsLabels.append("ht1000,mht450,nj3-5");
            self.nbinsLabels.append("ht1000,mht600,nj3-5");
            self.nbinsLabels.append("ht1250,mht200,nj3-5");
            self.nbinsLabels.append("ht1250,mht300,nj3-5");
            self.nbinsLabels.append("ht1250,mht450,nj3-5");
            self.nbinsLabels.append("ht1500,mht200,nj3-5");
            self.nbinsLabels.append("ht1500,mht300,nj3-5");
            
            self.nbinsLabels.append("ht500,mht200,nj6-7");
            self.nbinsLabels.append("ht500,mht300,nj6-7");
            self.nbinsLabels.append("ht500,mht450,nj6-7");
            self.nbinsLabels.append("ht800,mht200,nj6-7");
            self.nbinsLabels.append("ht800,mht300,nj6-7");
            self.nbinsLabels.append("ht800,mht450,nj6-7");
            self.nbinsLabels.append("ht1000,mht200,nj6-7");
            self.nbinsLabels.append("ht1000,mht300,nj6-7");
            self.nbinsLabels.append("ht1000,mht450,nj6-7");
            self.nbinsLabels.append("ht1250,mht200,nj6-7");
            self.nbinsLabels.append("ht1250,mht300,nj6-7");
            self.nbinsLabels.append("ht1250,mht450,nj6-7");
            self.nbinsLabels.append("ht1500,mht200,nj6-7");
            self.nbinsLabels.append("ht1500,mht300,nj6-7");

            self.nbinsLabels.append("ht500,mht200,nj8-99");
            self.nbinsLabels.append("ht800,mht200,nj8-99");
            self.nbinsLabels.append("ht1000,mht200,nj8-99");
            self.nbinsLabels.append("ht1250,mht200,nj8-99");
            self.nbinsLabels.append("ht1500,mht200,nj8-99");

        ## ------------------------
        ## hard-coded parameters
        self.nbins = len( self.nbinsLabels );
        self.ncategories = 5;
        ## ------------------------

    	self.filenames = [];
    	self.binContainers = [];

    	# define bin containers
    	for i in range(self.nbins):
    		cn = "T1tttt/T1tttt_mGo%i_mLSP%i_datacard_TEST_%s_bin%i.txt" % ( self.mGo,self.mLSP,self.anatype,i);
    		self.filenames.append(cn);
    		self.binContainers.append( binContainer(self.parseFileAndGetYields(cn),cn) );

		# fill histograms
		self.histos = [];
    	hn = "h_T1tttt_mGo%i_mLSP%i_datacard_TEST_%s_bin%i.txt" % ( self.mGo,self.mLSP,self.anatype,i);
    	for i in range(self.ncategories):
    		self.histos.append( ROOT.TH1F( hn+str(i), ";;yields",self.nbins,0,self.nbins ) );
    	for i in range(self.nbins):
    		curyields = self.binContainers[i].getYields();
    		for j in range(self.ncategories):
    			self.histos[j].SetBinContent(i+1, float(curyields[j]) );

    	# define stacks
    	self.sigHist = self.histos[0];
    	self.bkgHist = ROOT.THStack();
    	self.bkgHist.SetTitle(";;yield");
    	colors = [1,2,4,6,7,2];
    	for i in range(1,self.ncategories):
    		self.histos[i].SetFillColor( colors[i] );
    		self.histos[i].SetFillStyle( 1001 );
    		self.bkgHist.Add(self.histos[i]);



    def parseFileAndGetYields(self,cn):

    	f = open(cn,'r');
    	yields = [];
    	for lines in f:
    		if "rate" in lines:
    			yields = lines.split();
    			del yields[0];
    			
    	return yields;

    def makeCanvas(self,ymax = -99):

        banner = ROOT.TLatex(0.18,0.94,("m_{Gluino} = "+str(self.mGo)+", m_{LSP} = "+str(self.mLSP)));
        banner.SetNDC()
        banner.SetTextSize(0.05)

        for i in range(self.nbins):
            self.sigHist.GetXaxis().SetBinLabel(i+1,self.nbinsLabels[i]);
            #self.bkgHist.GetXaxis().SetBinLabel(i+1,self.nbinsLabels[i]);
        self.sigHist.GetXaxis().SetLabelSize(0.04);
        self.sigHist.GetXaxis().LabelsOption("v");

        ##--------------------------
        leg = ROOT.TLegend(0.72,0.7,0.92,0.9);
        leg.SetBorderSize(0);
        leg.SetFillStyle(0);
        leg.SetNColumns(2);
        for i in range(self.ncategories):
            if i == 0: leg.AddEntry(self.histos[i],self.ncategoriesNames[i],"p");
            if i >= 1: leg.AddEntry(self.histos[i],self.ncategoriesNames[i],"f");

    	c = ROOT.TCanvas("c","c",1400,1000);
    	self.sigHist.SetMaximum(self.bkgHist.GetStack().Last().GetMaximum()*100.);
        self.sigHist.Draw();
        self.bkgHist.Draw("histsames");
    	self.sigHist.SetMarkerStyle(24);
        self.sigHist.SetMarkerSize(2);        
    	self.sigHist.Draw("psames");
    	ROOT.gPad.SetLogy();
        leg.Draw();
        banner.Draw();
    	c.SaveAs("T1tttt/plots/Yield_"+str(self.mGo)+"_"+str(self.mLSP)+"_"+self.anatype+".pdf");
        c.SaveAs("T1tttt/plots/Yield_"+str(self.mGo)+"_"+str(self.mLSP)+"_"+self.anatype+".png");
        
        ##--------------------------
    	hSB1 = ROOT.TH1F("h_SB1",";;S/#sqrt{B}",self.nbins,0,self.nbins);
        hSB2 = ROOT.TH1F("h_SB2",";;S/#sqrt{B}",self.nbins,0,self.nbins);
        hSB3 = ROOT.TH1F("h_SB3",";;S/#sqrt{B}",self.nbins,0,self.nbins);
        for i in range(self.nbins):
            sb0 = self.sigHist.GetBinContent(i+1)/self.bkgHist.GetStack().Last().GetBinContent(i+1);
            if i >= 0 and i <=16:
                hSB1.SetBinContent(i+1,sb0);
                hSB2.SetBinContent(i+1,0);
                hSB3.SetBinContent(i+1,0);
            if i >= 17 and i <= 30:
                hSB1.SetBinContent(i+1,0);
                hSB2.SetBinContent(i+1,sb0);
                hSB3.SetBinContent(i+1,0);
            if i >= 31 and i <= 35:
                hSB1.SetBinContent(i+1,0);
                hSB2.SetBinContent(i+1,0);
                hSB3.SetBinContent(i+1,sb0);
            
            # hSB1.GetXaxis().SetBinLabel(i+1,self.nbinsLabels[i]);
            # hSB2.GetXaxis().SetBinLabel(i+1,self.nbinsLabels[i]);
            # hSB3.GetXaxis().SetBinLabel(i+1,self.nbinsLabels[i]);
        hSB1.GetXaxis().SetLabelSize(0.00); #hSB1.GetXaxis().LabelsOption("v");
        hSB2.GetXaxis().SetLabelSize(0.00); #hSB2.GetXaxis().LabelsOption("v");
        hSB3.GetXaxis().SetLabelSize(0.00); #hSB3.GetXaxis().LabelsOption("v");

        hSB1.SetFillStyle(3144); hSB2.SetFillStyle(3144); hSB3.SetFillStyle(3144);
        hSB1.SetFillColor(ROOT.kOrange); hSB2.SetFillColor(ROOT.kGreen+3); hSB3.SetFillColor(ROOT.kCyan+3);

        leg2 = ROOT.TLegend(0.25,0.7,0.55,0.85);
        leg2.SetBorderSize(0);
        leg2.SetFillStyle(0);
        leg2.AddEntry(hSB1,"njets = 3-5","f");
        leg2.AddEntry(hSB2,"njets = 6-7","f");
        leg2.AddEntry(hSB3,"njets > 8","f");       

        self.sigHist.GetXaxis().SetLabelSize(0.05);
        csb = ROOT.TCanvas("csb","csb",2000,2000);
        # csb.Divide(1,2);
        # csb.cd(1);
        pad1 = ROOT.TPad("pad1","pad1",0.00,0.55,1.00,1.00)
        pad2 = ROOT.TPad("pad2","pad2",0.00,0.00,1.00,0.55)
        pad1.SetFillColor(0)
        pad2.SetFillColor(0)
        pad1.Draw()
        pad2.Draw()
        pad1.SetBottomMargin(0.05);
        pad2.SetTopMargin(0.05);
        pad2.cd();         
        self.sigHist.Draw();
        self.bkgHist.Draw("histsames");
        self.sigHist.Draw("psames");
        ROOT.gPad.SetLogy();
        leg.Draw();
        #banner.Draw();        
        pad1.cd();
        hSB1.SetMaximum( 1.2*max(hSB1.GetMaximum(), hSB2.GetMaximum(), hSB3.GetMaximum()) );
	if ymax > 0: hSB1.SetMaximum(ymax);
        hSB1.Draw();
        hSB2.Draw("sames");
        hSB3.Draw("sames");
        leg2.Draw();
        banner.Draw();
        csb.SaveAs("T1tttt/plots/SB_"+str(self.mGo)+"_"+str(self.mLSP)+"_"+self.anatype+".pdf");
        csb.SaveAs("T1tttt/plots/SB_"+str(self.mGo)+"_"+str(self.mLSP)+"_"+self.anatype+".png");
        ##--------------------------

## ------------------------------------------------------------
## ------------------------------------------------------------
## ------------------------------------------------------------

if __name__ == '__main__':

    wp1_s = WorkingPointContainer( 1000, 1, "SMJ");
    wp1_s.makeCanvas(10);
    wp1_c = WorkingPointContainer( 1000, 1, "Classic");
    wp1_c.makeCanvas(10);

    wp2_s = WorkingPointContainer( 1025, 25, "SMJ");
    wp2_s.makeCanvas(10);
    wp2_c = WorkingPointContainer( 1025, 25, "Classic");
    wp2_c.makeCanvas(10);

    wp3_s = WorkingPointContainer( 1025, 825, "SMJ");
    wp3_s.makeCanvas(0.1);
    wp3_c = WorkingPointContainer( 1025, 825, "Classic");
    wp3_c.makeCanvas(0.1);

    wp4_s = WorkingPointContainer( 1025, 525, "SMJ");
    wp4_s.makeCanvas(1.2);
    wp4_c = WorkingPointContainer( 1025, 525, "Classic");
    wp4_c.makeCanvas(1.2);

