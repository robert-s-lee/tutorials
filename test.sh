set -x
# Call getopt to validate the provided input. 
options=$(getopt --long script: -- "$@")
[ $? -eq 0 ] || { 
    echo "Incorrect options provided"
    exit 1
}
eval set -- "$options"
while true; do
    echo $1
    case "$1" in
    --script)
        shift; # The arg is next in position args
        SCRIPT=$2
        echo $SCRIPT
        shift 2 ;;
    -- ) shift; break ;;
  esac
done
