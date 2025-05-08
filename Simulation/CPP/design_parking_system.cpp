class ParkingSystem {
    public:
        int ps[4];
        ParkingSystem(int big, int medium, int small) {
            ps[1] = big, ps[2] = medium, ps[3] = small;
        }

        bool addCar(int carType) {
            return ps[carType]-- > 0 ? true : false;
        }
    };

    /**
     * Your ParkingSystem object will be instantiated and called as such:
     * ParkingSystem* obj = new ParkingSystem(big, medium, small);
     * bool param_1 = obj->addCar(carType);
     */