## binning definition for sum jet mass analysis

from binning import *

extSMJbins = binning( [ "sumJetMass" , "HT" , "MHT" , "NJets" ] )

################ extSMJ cuts #### MHT cuts #### NJet cuts ###

## low MHT binning
extSMJbins.addBin( [ (0 , 200) , (500 , 9999) , (150 , 200) , (2 , 6) ] )
extSMJbins.addBin( [ (200 , 400) , (500 , 9999) , (150 , 200) , (2 , 6) ] )
extSMJbins.addBin( [ (400 , 600) , (500 , 9999) , (150 , 200) , (2 , 6) ] )
extSMJbins.addBin( [ (600 , 800) , (500 , 9999) , (150 , 200) , (2 , 6) ] )
extSMJbins.addBin( [ (800 , 9999) , (500 , 9999) , (150 , 200) , (2 , 6) ] )

extSMJbins.addBin( [ (0 , 200) , (500 , 9999) , (150 , 200) , (5 , 8) ] )
extSMJbins.addBin( [ (200 , 400) , (500 , 9999) , (150 , 200) , (5 , 8) ] )
extSMJbins.addBin( [ (400 , 600) , (500 , 9999) , (150 , 200) , (5 , 8) ] )
extSMJbins.addBin( [ (600 , 800) , (500 , 9999) , (150 , 200) , (5 , 8) ] )
extSMJbins.addBin( [ (800 , 9999) , (500 , 9999) , (150 , 200) , (5 , 8) ] )

extSMJbins.addBin( [ (0 , 200) , (500 , 9999) , (150 , 200) , (7 , 9999) ] )
extSMJbins.addBin( [ (200 , 400) , (500 , 9999) , (150 , 200) , (7 , 9999) ] )
extSMJbins.addBin( [ (400 , 600) , (500 , 9999) , (150 , 200) , (7 , 9999) ] )
extSMJbins.addBin( [ (600 , 800) , (500 , 9999) , (150 , 200) , (7 , 9999) ] )
extSMJbins.addBin( [ (800 , 9999) , (500 , 9999) , (150 , 200) , (7 , 9999) ] )

## low jet binning
extSMJbins.addBin( [ (0 , 200) , (500 , 9999) , (200 , 300)  , (2 , 6) ] )
extSMJbins.addBin( [ (0 , 200) , (500 , 9999) , (300 , 450)  , (2 , 6) ] )
extSMJbins.addBin( [ (0 , 200) , (500 , 9999) , (450 , 600)  , (2 , 6 ) ] )
extSMJbins.addBin( [ (0 , 200) , (500 , 9999) , (600 , 9999) , (2 , 6 ) ] )

extSMJbins.addBin( [ (200 , 400) , (500 , 9999) , (200 , 300)  , (2 , 6 ) ] )
extSMJbins.addBin( [ (200 , 400) , (500 , 9999) , (300 , 450)  , (2 , 6 ) ] )
extSMJbins.addBin( [ (200 , 400) , (500 , 9999) , (450 , 600)  , (2 , 6 ) ] )
extSMJbins.addBin( [ (200 , 400) , (500 , 9999) , (600 , 9999) , (2 , 6 ) ] )

extSMJbins.addBin( [ (400 , 600) , (500 , 9999) , (200 , 300)  , (2 , 6 ) ] )
extSMJbins.addBin( [ (400 , 600) , (500 , 9999) , (300 , 450)  , (2 , 6 ) ] )
extSMJbins.addBin( [ (400 , 600) , (500 , 9999) , (450 , 600)  , (2 , 6 ) ] )
extSMJbins.addBin( [ (400 , 600) , (500 , 9999) , (600 , 9999) , (2 , 6 ) ] )

extSMJbins.addBin( [ (600 , 800) , (500 , 9999) , (200 , 300)  , (2 , 6 ) ] )
extSMJbins.addBin( [ (600 , 800) , (500 , 9999) , (300 , 450)  , (2 , 6 ) ] )
extSMJbins.addBin( [ (600 , 800) , (500 , 9999) , (450 , 9999) , (2 , 6 ) ] )

extSMJbins.addBin( [ (800 , 9999) , (500 , 9999) , (200 , 300)  , (2 , 6 ) ] )
extSMJbins.addBin( [ (800 , 9999) , (500 , 9999) , (300 , 9999) , (2 , 6 ) ] )

## medium jet binning
extSMJbins.addBin( [ (0 , 200) , (500 , 9999) , (200 , 300)  , (5 , 8) ] )
extSMJbins.addBin( [ (0 , 200) , (500 , 9999) , (300 , 450)  , (5 , 8) ] )
extSMJbins.addBin( [ (0 , 200) , (500 , 9999) , (450 , 9999)  , (5 , 8) ] )

extSMJbins.addBin( [ (200 , 400) , (500 , 9999) , (200 , 300)  , (5 , 8) ] )
extSMJbins.addBin( [ (200 , 400) , (500 , 9999) , (300 , 450)  , (5 , 8) ] )
extSMJbins.addBin( [ (200 , 400) , (500 , 9999) , (450 , 9999)  , (5 , 8) ] )

extSMJbins.addBin( [ (400 , 600) , (500 , 9999) , (200 , 300)  , (5 , 8) ] )
extSMJbins.addBin( [ (400 , 600) , (500 , 9999) , (300 , 450)  , (5 , 8) ] )
extSMJbins.addBin( [ (400 , 600) , (500 , 9999) , (450 , 9999)  , (5 , 8) ] )

extSMJbins.addBin( [ (600 , 800) , (500 , 9999) , (200 , 300)  , (5 , 8) ] )
extSMJbins.addBin( [ (600 , 800) , (500 , 9999) , (300 , 450)  , (5 , 8) ] )
extSMJbins.addBin( [ (600 , 800) , (500 , 9999) , (450 , 9999) , (5 , 8) ] )

extSMJbins.addBin( [ (800 , 9999) , (500 , 9999) , (200 , 300)  , (5 , 8) ] )
extSMJbins.addBin( [ (800 , 9999) , (500 , 9999) , (300 , 9999) , (5 , 8) ] )

## high jet binning
extSMJbins.addBin( [ (0 , 200)  , (500 , 9999) , (200 , 9999)  , (7 , 9999) ] )
extSMJbins.addBin( [ (200 , 400)  , (500 , 9999) , (200 , 9999)  , (7 , 9999) ] )
extSMJbins.addBin( [ (400 , 600)  , (500 , 9999) , (200 , 9999)  , (7 , 9999) ] )
extSMJbins.addBin( [ (600 , 800)  , (500 , 9999) , (200 , 9999)  , (7 , 9999) ] )
extSMJbins.addBin( [ (800 , 9999) , (500 , 9999) , (200 , 9999)  , (7 , 9999) ] )
