import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_100_1_NMT.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_101_1_ynF.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_102_1_Y86.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_103_1_Qve.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_104_1_evX.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_105_1_F8b.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_106_1_Rz9.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_107_1_oD6.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_108_1_fOa.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_109_1_0vr.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_10_1_2OT.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_110_1_3P4.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_111_1_cEQ.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_112_1_SpT.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_113_1_gB4.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_114_1_LnT.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_115_1_oQg.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_11_1_RSt.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_12_1_CLL.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_13_1_ljJ.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_14_1_eKk.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_15_1_d4d.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_16_1_F5b.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_17_1_030.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_18_1_TTY.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_19_1_PuA.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_1_1_th4.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_20_1_aLM.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_21_1_ADo.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_22_1_kpW.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_23_1_E3N.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_24_1_Lc0.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_25_1_4FJ.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_26_1_VWH.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_27_1_1mc.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_28_1_GAd.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_29_1_dyN.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_2_1_sk8.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_30_1_Seg.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_31_1_5gG.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_32_1_uxt.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_33_1_vVl.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_34_1_ANO.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_35_1_0aK.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_36_1_DUj.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_37_1_ATx.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_38_1_61t.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_39_1_Hyw.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_3_1_pdt.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_40_1_ObF.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_41_1_wqP.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_42_1_mXT.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_43_1_Zum.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_44_1_vwh.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_45_1_2at.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_46_1_Xld.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_47_1_9zH.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_48_1_PzY.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_49_1_BvY.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_4_1_eqR.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_50_1_V4s.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_51_1_HjW.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_52_1_hmU.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_53_1_pBN.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_54_1_OQF.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_55_1_hgl.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_56_1_ir7.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_57_1_k6u.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_58_1_N8N.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_59_1_Id4.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_5_1_zGY.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_60_1_sFu.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_61_1_Kh8.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_62_1_KQJ.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_63_1_Ghi.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_64_1_fTE.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_65_1_2tu.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_66_1_Fbo.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_67_1_fWu.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_68_1_LPa.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_69_1_dCc.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_6_1_7G1.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_70_1_nKB.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_71_1_nXq.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_72_1_Jsk.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_73_1_YJ4.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_74_1_Yk1.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_75_1_TLI.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_76_1_Pb4.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_77_1_1KY.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_78_1_UEl.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_79_1_Ua1.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_7_1_hbH.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_80_1_P1t.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_81_1_ZEb.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_82_1_Esa.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_83_1_mzB.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_84_1_goR.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_85_1_17I.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_86_1_YKc.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_87_1_Z8f.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_88_1_rZW.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_89_1_ftM.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_8_1_6hp.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_90_1_Fd5.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_91_1_BLn.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_92_1_Qnt.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_93_1_scr.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_94_1_NuN.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_95_1_O4W.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_96_1_GWx.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_97_1_HVy.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_98_1_Bm9.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_99_1_klW.root',
    'file:/nfs/bluearc/group/skims/hww/Zgamma_2l/hwwSkim_9_1_6dO.root',
] );


secFiles.extend( [
               ] )

