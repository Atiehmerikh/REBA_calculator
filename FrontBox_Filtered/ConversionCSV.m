data = loadbvh('ResultFrontBox_Filtered.bvh');

for i = 1:length(data) %You run over each line in data. Each line represents one joint
    if isempty(data(i).trans(:,:,1)) ~= 1  %You can only do following code if data.trans contains matrices
        FolderName = data(i).name; 
        mkdir(FolderName); %Create a folder with the name of the joint you're considering
        mkdir(FolderName,'Translation Matrix'); 
        mkdir(FolderName,'Rotation Matrix');
        Nframes = data(i).Nframes;
        for j = 1:Nframes %Loop over every frame
            M = data(i).trans(:,:,j);
            R = M(1:3,1:3); %This takes the 3x3 rotation matrix in M
            T = M(1:3,4); %This takes the 3x1 translation matrix in M

            nameR = sprintf('RotationMatrixFrame%d.csv', j);
            nameT = sprintf('TranslationMatrixFrame%d.csv', j);

            f_R = fullfile('c:\','Users','jihad','Documents','VUB','Master 1','MA1 Project','matlab','ConversionToCSV','FrontBox_Filtered',FolderName,'Rotation Matrix',nameR);
            f_T = fullfile('c:\','Users','jihad','Documents','VUB','Master 1','MA1 Project','matlab','ConversionToCSV','FrontBox_Filtered',FolderName,'Translation Matrix',nameT);

            writematrix(R,f_R);
            writematrix(T,f_T);
        end
    end  
end
