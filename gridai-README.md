# grid-monai

Run Monai [exmaples](https://github.com/Project-MONAI/tutorials) 

for file in $(find 2d* 3d* -name "*eval*.py" -print); do
  echo $file
  python $file
  if [ $? -ne 0 ]; then
    echo "$file" >> runbad.log
  else
    echo "$file" >> rungood.log
  fi  
done

for file in "3d_classification/torch"/*train* "3d_classification/ignite"/*train* "2d_segmentation/torch"/*train* "3d_segmentation/torch"/*train* "3d_segmentation/ignite"/*train*; do
  echo $file
  python $file
  if [ $? -ne 0 ]; then
    echo "$file" >> runbad.log
  else
    echo "$file" >> rungood.log
  fi
done

# this does not exists
for file in "modules/workflows"/*train*

# Setup Environment

```bash
conda create --yes --name monai python=3.8
conda activate monai
git clone https://github.com/Project-MONAI/tutorials
cd tutorials
pip install -r gridai-requirements.txt
pip install lightning-grid
grid login
```

```bash
export MONAI_TB_DIR=./lightning_logs/monai
export MONAI_MAX_EPOCHS=1
export MONAI_DATA_DIR=./

# ignite eval looks for min of MONAI_MAX_EPOCHS=4
runexmaples.sh
```

```bash
grid run runexamples.sh
```