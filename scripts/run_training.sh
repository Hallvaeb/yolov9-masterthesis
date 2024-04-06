# bash scripts/run_training.sh

python train_dual.py \
--batch 16 --epochs 5 --img 640 --device cpu --min-items 0 --close-mosaic 15 \
--data ./data/fimus1_yolo.yaml \
--weights ./weights/yolov9-e.pt